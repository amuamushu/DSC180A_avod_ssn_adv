import sys
import os
import json

from avod_ssn.avod.experiments import run_evaluation, run_inference, run_training
from utils import avod_utils

def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''
    if 'test' in targets:
        with open('config/test.json') as fh:
            test_config = json.load(fh)

        # make the data target
        avod_utils.run_main_with_command_line_args(run_training, **test_config['training])
        avod_utils.run_main_with_command_line_args(run_inference, **(test_config['inference']))

    if 'clean' in targets:
        for file in os.listdir('outputs'):
            os.remove(os.path.join(dir, file))
    return


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)