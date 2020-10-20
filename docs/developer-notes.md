# TODO

## Next step

  - Fix issues with `flake8 --max-line-length=110 code`

## Code

    * test GUI
    - optional
      - fix flake8 warning (newer version of flake8 and/or pycodestyle=2.4+)
      - remove log files in the end of the test (or create them in folder)
      - implement one more topic as an excersize
      - overall code cleaning

## Infrastructure

    * update lab guides for Python language
    - decide whether to use Python virtualenv
    - change license to MIT or something like that
    - enable macOS testing on Travis CI

# NOTES

    - Python virtual environment
      $ python3 -m venv tutorial-env
      $ source tutorial-env/bin/activate
      $ deactivate # if needed


    - Dependencies installation
       69  easy_install pip
       70  sudo easy_install pip
       95  pip install -r requirements.txt

   80  python -m pip install flake8
   87  pip install zipp==0.5.0
   88  pip install contextlib2 pathlib2
   89  pip install configparser==3.5
   99  PATH="/Users/kirill-personal/Library/Python/2.7/bin:$PATH"

    - list available versions of the package
      $ pip3 install flake8==