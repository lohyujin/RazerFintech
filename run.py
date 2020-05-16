#!/usr/bin/env python3
from flaskbank.backend import create_app
from flaskbank.backend.config import ProductionConfig
import argparse


def main():
    parser = argparse.ArgumentParser(description='Flask Bank Project',
                                     epilog='Default: run on local machine, '
                                            'debug on')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-p', '--production', action='store_true',
                       help='Production mode, debug off')
    args = parser.parse_args()

    production = args.production

    if production:
        print('Using Production Configuration')
        create_app(ProductionConfig).run(threaded=True, host="0.0.0.0")
    else:
        print('Using Development Configuration')
        create_app().run(threaded=True, host="0.0.0.0")


if __name__ == '__main__':
    main()
