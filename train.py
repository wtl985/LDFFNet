# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings('ignore')
from LDFFNet import RTDETR


if __name__ == '__main__':

    model = RTDETR(model=r'/LDFFNet/cfg/models/LDFFNet.yaml')
    #model.load('LDFFNet.pt')
    model.train(data=r'/LDFFNet/jiazawu.yaml',
                imgsz=640,
                epochs=300,
                batch=16,
                project='runs/train',
                name='exp',
                workers=0,
                amp=False
                )
