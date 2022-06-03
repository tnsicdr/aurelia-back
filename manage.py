#!/usr/bin/env python3
from flask.cli import main 
import os

if __name__ == '__main__':
  os.environ['FLASK_APP'] = 'core'
  os.environ['FLASK_DEBUG'] = 'true'
  main()