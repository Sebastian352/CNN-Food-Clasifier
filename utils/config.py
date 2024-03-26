import os

ORIG_INPUT_DATASET = "Food-5K"

BASE_PATH = "dataset"

TRAIN = "training"
TEST = "evaluation"
VAL = "validation"

CLASSES = ["non-food", "food"]

BATCH_SIZE = 32

LE_PATH = os.path.sep.join(["output", "le.cpickle"])
BASE_CSV_PATH = "output"

MODEL_PATH = os.path.sep.join(["output", "model.cpickle"])
