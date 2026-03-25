LDFFNet:A Transformer Driven Lightweight Network with Dynamic Feature Fusion for Microstructural Inclusion Detection in Aluminum Alloys

The detection and characterization of microscopic inclusions in aluminum alloys have become increasingly critical as aerospace and precision manufacturing industries impose stricter requirements for material purity. Conventional human inspection approaches fall short of meeting high precision detection demands involving small scale objects, partially obscured targets, and specimens with weak contrast. To tackle this issue, the present work introduces an intelligent recognition framework built upon a Transformer driven lightweight dynamic feature fusion network, marking a advancement in the microscopic detection of inclusions within aluminum alloy materials. The proposed method effectively integrates a lightweight backbone network with the SD Loss function and incorporates a dynamic feature weighting fusion module. This approach not only achieves model lightweight design but also enhances the extraction of critical region features, enabling adaptive feature interaction and enhancement while strengthening the network capability to capture effective information. Experimental results reveal that the presented approach attains a detection accuracy of 90.8\% on the mAP@0.5 metric, reflecting a gain of 4.5 percentage points compared to standard Transformer-based methods. Regarding the more rigorous mAP@0.5:0.95 metric, the method reaches 60.8\%, corresponding to a performance gain of 5.3 percentage points. Additionally, ablation studies further confirm the validity of each component within the proposed method. This research provides a lightweight and high performance solution for automated microstructural detection of alloy materials, holding significant theoretical importance and practical value for enhancing material quality control and accelerating new material development.

<img width="964" height="449" alt="image" src="https://github.com/user-attachments/assets/f7ac5799-4f51-43ec-a374-ca0037757cb5" />


Visual result comparison of six aluminum alloy inclusion categories across different backbone networks, namely VGG-16, Darknet53, GELAN, CSPNet, LSKNet, and R-ELAN.
<img width="1526" height="1273" alt="fig6" src="https://github.com/user-attachments/assets/49fb1171-d235-4849-81da-019eadf4d006" />
![fig6](https://github.com/user-attachments/assets/65371b85-ffba-4d22-a153-f7b23795639b)

Evolution of mAP@0.5 and mAP@[0.5:0.95] metrics throughout the training process across different detection approaches.
<img width="927" height="402" alt="image" src="https://github.com/user-attachments/assets/85a6b154-67db-4792-af7b-65c03791f4c0" />


The relationship between inference latency and both mAP and FLOPs indicators.
<img width="947" height="398" alt="image" src="https://github.com/user-attachments/assets/932e532e-bc8d-44a6-b082-fe748a09170c" />



