import os

import basically_ti_basic as btb

# get all the files in compiled
compiled_files = os.listdir("compiled")

# create src dir if it doesn't exist
if not os.path.exists("src"):
    os.makedirs("src")

# decompile each file
for file in compiled_files:
    btb.decompile_file("compiled/" + file, "src/" + file)
