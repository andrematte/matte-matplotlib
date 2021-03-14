# Script to install the Matte Theme for Matplotlib
# Created by: André Matte (https://github.com/andrematte)

# %% Import Libraries
import matplotlib
import shutil
import os

# %% Gets Matplotlib configuration directory
config_dir = matplotlib.get_configdir()

# %% Creates style directory and install theme

try:
    os.mkdir(f'{config_dir}/stylelib/')
except:
    pass

shutil.copyfile('./Matte.mplstyle', f'{config_dir}/stylelib/Matte.mplstyle')

print(f'Theme installed to {config_dir}/stylelib/Matte.mplstyle !')
