#!/usr/bin/env python3

# Author ID: kdam3

import subprocess

def free_space():
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, text=True, capture_output=True)

    return result.stdout.strip()

if __name__ == "__main__":
    # Print the free space when the script is executed directly
    print(free_space())

import lab3d
print(lab3d.free_space())
