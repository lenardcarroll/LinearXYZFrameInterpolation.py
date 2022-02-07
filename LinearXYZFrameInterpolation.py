#All modules to be used imported
import argparse
import pandas as pd
import numpy as np
import csv

#Cheat sheet of arguments to be used with the script
parser = argparse.ArgumentParser()
parser.add_argument("-inp", "--input", dest = "input", default = "input.xyz", help="Name of input file")
parser.add_argument("-out", "--output", dest = "output", default = "output.xyz", help="Name of output file")
parser.add_argument("-rep", "--replicas", dest = "Num_Replicas", default = "10", help="Enter the number of structures to interpolate")
args = parser.parse_args()

#Here the number of atoms is determined by reading in the first value of the xyz file, the number of lines for the whole file is determined and the number of frames calculated using the aforementioned two variables
with open(args.input) as f:
    lines = f.read()
    first = lines.split('\n', 1)[0]
num_of_atoms = int(first)
num_of_lines = len(list(open(args.input)))
num_of_frames = int(num_of_lines/(num_of_atoms+2))
Num_Replicas = int(args.Num_Replicas)

#Here the headers of the xyz file is removed
skiparray = []
for i in range(num_of_frames):
    k = num_of_atoms*i+2*i
    skiparray.append(k)
    skiparray.append(k+1)
df = pd.read_csv(args.input, skiprows=skiparray, names=['Atom', 'X', 'Y', 'Z'], sep="\s+" , engine='python')

#Here the dataframe is split into multiple dataframes, each making up a frame from the file
frames = [ df.iloc[i*num_of_atoms:(i+1)*num_of_atoms].copy() for i in range(num_of_frames+1) ]

#Here we save the first frame to the user's specificed output file
with open(args.output,"w") as f:
    print(num_of_atoms, file=f)
    print("XYZ file created with LinearXYZFrameInterpolation.py", file=f)
    for j in frames[0].index:
        print(frames[0]['Atom'].iloc[j], frames[0]['X'].iloc[j], frames[0]['Y'].iloc[j], frames[0]['Z'].iloc[j], file=f)

#Here we append all the other frames to the file, including the interpolated ones
with open(args.output, "a") as f:
    for i in range(1,num_of_frames):
        frames[i] = frames[i].reset_index(drop=True)
        X, Y, Z = (frames[i]['X'] - frames[i-1]['X'])/(Num_Replicas-1), (frames[i]['Y'] - frames[i-1]['Y'])/(Num_Replicas-1), (frames[i]['Z'] - frames[i-1]['Z'])/(Num_Replicas-1)
        for k in range(1,Num_Replicas):
            X1, Y1, Z1 = frames[i-1]['X'] + X*k, frames[i-1]['Y'] + Y*k, frames[i-1]['Z'] + Z*k
            print(num_of_atoms, file=f)
            print("XYZ file created with LinearXYZFrameInterpolation.py", file=f)
            for j in frames[0].index:
                print(frames[0]['Atom'].iloc[j], X1.iloc[j], Y1.iloc[j], Z1.iloc[j], file=f)