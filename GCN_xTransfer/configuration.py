import os
import datetime
import numpy as np
import tensorflow as tf

## These lines ensure any existing tf sessions are closed.
try:
    tf.Session().close()
except:
    pass

## Numpy print options
np.set_printoptions(precision=3)

# Epitope of paratope prediction
mode_experiment = "epitope"
#mode_experiment = "paratope"

## Directories

# path to yml files
experiment_directory = "experiments/"

# path to cpkl files
data_directory = "../data/data_epitope"
# data_directory = "../data/data_paratope"

# path to output directory
output_directory = "../results_final/results_epitope_xTransfer/"
#output_directory = "../results_final/results_paratope_xTransfer/"

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# A slightly fancy printing method
def printt(msg):
    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("{}| {}".format(time_str, msg))
