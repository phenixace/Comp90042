# Group Project - Comp90042: Natural Language Processing 

## Contributors
1. Jiatong Li 
2. Sherry Wang 
3. Moxuan Zhang 

## Dependecies
* pytorch 1.9.0 + cuda 11.1
* paddlenlp 2.0.8
* paddlepaddle-gpu 2.1.2.post112
* transformers 4.10.0
## Usage

### Training pytorch based Roberta, Bart, Bert models
```
python main.py
  -h, --help            show this help message and exit
  --random_seed RANDOM_SEED
                        Choose random_seed
  --model MODEL         Sevral models are available: Bart | Bert | T5
  --model_path MODEL_PATH
                        use local model weights if specified
  --save_path SAVE_PATH
                        where to save the model
  --total_steps TOTAL_STEPS
                        Set training steps
  --eval_steps EVAL_STEPS
                        Set evaluation steps
  --batch_size BATCH_SIZE
                        Set batch size
  --lr LR               Set learning rate
  --optim OPTIM         Choose optimizer
  --warmup_steps WARMUP_STEPS
                        WarmUp Steps
  --lrscheduler         Apply LRScheduler
  --mode MODE           train, test, or inference
  --device DEVICE       Device
```

### Training paddle based model SKEP
See the instructions in `skep.ipynb`

## Reference
* Hugging Face Co.
* Baidu Paddlenlp
