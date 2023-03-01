# Object-Detection-with-YOLOX-and-SE-module

### Introduction
use YOLOX model and add SELayers into interval of darknet2、darknet3、
darknet4、darknet5 to detect the car object.
![](https://i.imgur.com/paHwszM.jpg)


### How to use

1. put data set into Object-Detection-with-YOLOX-and-SELayer/datasets/coco_car
there are 3 folders inside the coco_car folder

```
annotations(json.)
train2017(train images)
val2017(validation images)
```

2. train model

```
python tools/train.py -f exps/example/custom/yolox_s.py -d 1 -b 8 --fp16 -o -c 
yolox_s.pth
```

3. test new images

```
python tools/demo.py image -f exps/example/custom/yolox_s.py -c 
YOLOX_outputs/yolox_s/best_ckpt.pth --path datasets/test_data/test --conf 0.25 --
nms 0.5 --tsize 640 --save_result --device [gpu]
```

4. generate mAP
```
python tools/demo.py image -f exps/example/custom/yolox_s.py -c 
YOLOX_outputs/yolox_s/best_ckpt.pth --path datasets/test_data/test --conf 0.25 --
nms 0.5 --tsize 640 --save_result --device [gpu]

```


### Reference
https://github.com/Megvii-BaseDetection/YOLOX
