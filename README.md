# CS 585 CycleGAN Final Project

# Collaborators:
John Mcdonough
Phuong Khanh Tran

# Goal

Our goal is to perform image-to-image translation on an unpaired dataset of optical coherence tomography (OCT) brain scan images and images of brain tissues treated via Gallyas silver staining. Our approach would be to implement a diffusion model using the dataset to perform unsupervised “digital staining” on the OCT scans. 

Both OCT and Gallyas silver stain can visualize myelin tissue structure in the brain. OCT is a non-invasive imaging technique, while Gallyas silver stain requires the brain to be sliced and treated through a complicated process. A digital staining approach eliminates the need for invasive and error-prone techniques but still provides the highly descriptive images of the brain tissue possible with such an approach. 

This work would expand on a project currently in research at the Computational Imaging Systems Lab (CISL) at Boston University. Other lab members have approached the digital staining problem using Cycle-Consistent Generative Adversarial Networks (Cycle-GAN) and Contrastive Unpaired Image-to-Image Translation (CUT). We would apply CycleGAN model, optimize hyperparameters and output metrics for this new approach, and evaluate whether it leads to improved performance.

# Data
In our experiments, we used the dataset from CISL

# Presentation
https://docs.google.com/presentation/d/1ktzwCI8lbpFUkPfok3ocVq5GxlDVPm1xVYCZ0k6l8As/edit?usp=sharing

# Report
https://docs.google.com/document/d/1Kr_QhiYAdiByXxYxigQDwORLauoqgCfieochDsIpUL4/edit?usp=sharing

# Citation: 
@inproceedings{CycleGAN2017,
  title={Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networkss},
  author={Zhu, Jun-Yan and Park, Taesung and Isola, Phillip and Efros, Alexei A},
  booktitle={Computer Vision (ICCV), 2017 IEEE International Conference on},
  year={2017}
}
