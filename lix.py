import argparse
import logging

from delfick_project.logging import setup_logging
from photons_app.executor import library_setup

import operations
import validations

OPERATIONS = { 'list', 'describe', 'remember', 'forget', 'on', 'off', 'hsv', 'hue', 'saturation', 'brightness', 'rgb', 'red', 'green', 'blue', 'warmth' }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', choices=OPERATIONS)
    parser.add_argument('target', nargs='?')
    parser.add_argument('value', nargs='?')
    args = parser.parse_args()

    setup_logging(level=logging.ERROR)
    collector = library_setup()

    validate = getattr(validations, args.operation)
    operate = getattr(operations, args.operation)

    try:
        validate(args)
    except Exception:
        print('PLACEHOLDER: usage should be printed here')
        pass

    collector.run_coro_as_main(operate(collector, args))
