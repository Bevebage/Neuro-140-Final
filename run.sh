#!/bin/bash

# Total number of episodes:          1000000
# Total number of training episodes: 100000
# Level:                             mediumClassic

python pacman.py -p PacmanDQN -n 5000 -x 4000 -l smallGrid
