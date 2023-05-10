import torch
import torchvision.transforms as transforms

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
TRAIN_DIR = "CISL_Dataset/Train_Data"
VAL_DIR = "CISL_Dataset/Train_Data"
BATCH_SIZE = 1
LEARNING_RATE = 2e-4
LAMBDA_CYCLE = 10
NUM_WORKERS = 4
NUM_EPOCHS = 200
LOAD_MODEL = False
SAVE_MODEL = True
CHECKPOINT_G_GSS = "g_gss.pth.tar"
CHECKPOINT_F_OCT = "f_oct.pth.tar"
CHECKPOINT_DISC_GSS = "disc_gss.pth.tar"
CHECKPOINT_DISC_OCT = "disc_oct.pth.tar"

transforms = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Resize((256, 256)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ],
)