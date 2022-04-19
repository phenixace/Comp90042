import re
import torch

def clean_text(text):
    # clean @at, namely clean username
    text = re.sub('@[^\s]+', '', text)
    # clean URLs
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', text)
    # clean numbers
    text = re.sub('[0-9]+', '', text)
    # lower if neccessary
    # remove non-english words if neccessary
    text = re.sub('[^a-z^A-Z^ ^,^.^!^?^’]', '', text)
    text = re.sub('  ', ' ', text)
    return text.lower()

class FixedScheduler(torch.optim.lr_scheduler.LambdaLR):
    def __init__(self, optimizer, last_epoch=-1):
        super(FixedScheduler, self).__init__(optimizer, self.lr_lambda, last_epoch=last_epoch)
    def lr_lambda(self, step):
        return 1.0


class WarmupLinearScheduler(torch.optim.lr_scheduler.LambdaLR):
    def __init__(self, optimizer, warmup_steps, scheduler_steps, min_ratio, fixed_lr, last_epoch=-1):
        self.warmup_steps = warmup_steps
        self.scheduler_steps = scheduler_steps
        self.min_ratio = min_ratio
        self.fixed_lr = fixed_lr
        super(WarmupLinearScheduler, self).__init__(
            optimizer, self.lr_lambda, last_epoch=last_epoch
        )

    def lr_lambda(self, step):
        if step < self.warmup_steps:
            return (1 - self.min_ratio)*step/float(max(1, self.warmup_steps)) + self.min_ratio

        if self.fixed_lr:
            return 1.0

        return max(0.0,
            1.0 + (self.min_ratio - 1) * (step - self.warmup_steps)/float(max(1.0, self.scheduler_steps - self.warmup_steps)),
        )

