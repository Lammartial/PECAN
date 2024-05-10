import os
import cPickle
import yaml
from configuration import experiment_directory, data_directory, printt
import pandas as pd

# pre-process to include residue indices
def preProcessData(data):
    num_complex = len(data)
    for idx_complex in range(num_complex):

        # Use only up to 15 neighbors during convolution
        data[idx_complex]["l_hood_indices"] = data[idx_complex]["l_hood_indices"][:,:15,:]
        data[idx_complex]["r_hood_indices"] = data[idx_complex]["r_hood_indices"][:,:15,:]

        data[idx_complex]["l_edge"] = data[idx_complex]["l_edge"][:,:15,:]
        data[idx_complex]["r_edge"] = data[idx_complex]["r_edge"][:,:15,:]

# Remove antigens as primary protein
def remove_ags(data):
    printt("Removing Ags")
    new_data = []
    for data_idx in range(len(data)):
        if data_idx % 2 == 1:
            new_data.append(data[data_idx])
    return new_data

# Remove antibodies as primary protein
def remove_abs(data):
    printt("Removing Abs")
    new_data = []
    for data_idx in range(len(data)):
        if data_idx % 2 == 0:
            new_data.append(data[data_idx])
    return new_data


exp_file = "node_edge_conv2.yml"
printt("Running Experiment File: {}".format(exp_file))
f_name = exp_file.split(".")[0] if "." in exp_file else exp_file
exp_specs = yaml.load(open(os.path.join(experiment_directory, exp_file), 'r').read())


for name, experiment in exp_specs["experiments"]:
    test_data_file = os.path.join(data_directory, experiment["test_data_file"])

    printt("Loading test data")
    test_data = cPickle.load(open(test_data_file))
    preProcessData(test_data)
    test_data = remove_abs(test_data)
    print(test_data)



