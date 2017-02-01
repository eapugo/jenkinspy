#!/bin/bash
#install python venv on jenkins slave

PYENV_HOME=$WORKSPACE/.saltpyenv/

# Delete previously built virtualenv
if [ -d $PYENV_HOME ]; then
    rm -rf $PYENV_HOME
fi

# Create virtualenv and install necessary packages
virtualenv --no-site-packages $PYENV_HOME
. $PYENV_HOME/bin/activate
pip install salt-pepper
pip install request
