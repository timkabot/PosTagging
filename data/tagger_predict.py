# python3.7 tagger_predict.py <test_file_absolute_path> <model_file_absolute_path> <output_file_absolute_path>

import os
import sys
import torch
import numpy as np
import pickle


def tag_sentence(test_file, model_file, out_file):
    # write your code here. You can add functions as well.
    # use torch library to load model_file
    print('Finished...')


if __name__ == "__main__":
    # make no changes here
    test_file = sys.argv[1]
    model_file = sys.argv[2]
    out_file = sys.argv[3]
    tag_sentence(test_file, model_file, out_file)
