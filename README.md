# CS-585-Final-Project

# Goal

Our goal is to perform image-to-image translation on an unpaired dataset of optical coherence tomography (OCT) brain scan images and images of brain tissues treated via Gallyas silver staining. Our approach would be to implement a diffusion model using the dataset to perform unsupervised “digital staining” on the OCT scans. 

Both OCT and Gallyas silver stain can visualize myelin tissue structure in the brain. OCT is a non-invasive imaging technique, while Gallyas silver stain requires the brain to be sliced and treated through a complicated process. A digital staining approach eliminates the need for invasive and error-prone techniques but still provides the highly descriptive images of the brain tissue possible with such an approach. 

This work would expand on a project currently in research at the Computational Imaging Systems Lab (CISL) at Boston University. Other lab members have approached the digital staining problem using Cycle-Consistent Generative Adversarial Networks (Cycle-GAN) and Contrastive Unpaired Image-to-Image Translation (CUT). We would apply more recent diffusion models, optimize hyperparameters and output metrics for this new approach, and evaluate whether it leads to improved performance.

# Data
In our experiments, we used the following datasets:
* 3D brain MR images: [OASIS-3 dataset](https://www.oasis-brains.org/)

# Citation
@inproceedings{kim2022diffusemorph,
  title={DiffuseMorph: Unsupervised Deformable Image Registration Using Diffusion Model},
  author={Kim, Boah and Han, Inhwa and Ye, Jong Chul},
  booktitle={European Conference on Computer Vision},
  pages={347--364},
  year={2022},
  organization={Springer}
}
