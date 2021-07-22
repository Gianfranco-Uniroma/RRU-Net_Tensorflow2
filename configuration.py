# Dataset
DATA_DIR = "/content/data/"
PRISTINE_FOLDER = ""
FORGERED_FOLDER = "Tp"
GROUND_TRUTH_FOLDER = "Gt"
DATASET_NAME = "Spliced_COCO"
DATASET_SIZE = 180
IMG_SHAPE = (384, 256)
IMG_CHANNELS = 3

# Training
#TRAIN_PERCENT = 0.70
#VAL_PERCENT = 0.10
#TEST_PERCENT = 0.20
TRAIN_SIZE = 125
VAL_SIZE = 10
TEST_SIZE = 45
BATCH_SIZE = 6
EPOCHES = 50

# Learning
MOMENTUM = 0.9
WEIGHT_DECAY = 0.0005
LEARNING_RATE = 0.1

# Noise attack
NOISE_VARIANCE = 0.002
COMPRESSION_QUALITY = 100
