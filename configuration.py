# Dataset
DATA_DIR = "./data"
PRISTINE_FOLDER = "Pristine"
FORGERED_FOLDER = "Forgered"
GROUND_TRUTH_FOLDER = "Ground_Truth"
DATASET_NAME = "Realistic_Tampering_Dataset"
DATASET_SIZE = 220
IMG_SHAPE = (384, 256)
IMG_CHANNELS = 3

# Training
TRAIN_PERCENT = 0.70
VAL_PERCENT = 0.10
TEST_PERCENT = 0.20
BATCH_SIZE = 10

# Learning
MOMENTUM = 0.9
WEIGHT_DECAY = 0.0005
LEARNING_RATE = 0.1

# Noise attack
NOISE_VARIANCE = 0.002
COMPRESSION_QUALITY = 100