import os

IMAGE_SIZE = 128
SCREEN_SIZE = 768
NUM_TILES_SIDE = 6
NUM_TILES_TOTAL = 36
MARGIN = 2

ASSET_DIR = 'assets'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
assert len(ASSET_FILES) == 18
