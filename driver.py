import argparse
import os
import sys
import traceback

def setup_args():
    '''Constructs the command line argument setup.'''
    parser = argparse.ArgumentParser()

    parser.add_argument('method', choices=['phasecorrelation'], default='phasecorrelation',
        help='The methodology for stabilizing the video.')
    parser.add_argument('input-video', required=True, help='The source video to be stabilized.')
    parser.add_argument('output-file', required=True, help='The location to put the output file.')

    return parser.parse_args()

def validate_args(args):
    '''Validates the correctness of the provided arguments.'''
    if not os.path.isfile(os.path.expanduser(args.input_video)):
        return 'The input video does not appear to be a valid file.'

    return True

def main():
    '''The main entry point for the program.'''
    args = setup_args()

    # Validate the arguments.
    result = validate_args(args)
    if result is not True:
        return result
    
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        sys.exit(traceback.format_exc())
