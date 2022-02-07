# LinearXYZFrameInterpolation.py

Do you have at least frames and you'd like to interpolate more frames in-between these frames, perhaps to roughly understand the change between the frames better or perhaps you want to create a smooth video for presentation purposes? Then this this script for you. The script works using the following general command:

```
python -i LinearXYZFrameInterpolation.py -in <INPUT_STRUCTURE_FILE_NAME> -out <OUTPUT_STRUCTURE_FILE_NAME> -rep <HOW_MANY_FRAMES_TO_INTERPOLATE>
```

Before running the script, make sure to install the necessary modules/packages as:

```
pip install -r requirements.txt
```

The script works by reading in the .xyz file as a dataframe, removing the headers from each frame and then splitting dataframe up into smaller dataframes, these being the frames from the .xyz file. Next, the distance between the atoms from frame n to frame n+1 is calculated, then deivided by the number of frames you want to interpolate minus one, that is:

( r<sub>(n+1)</sub> - r<sub>n</sub>)/(#InterpolatedFrames - 1)
  
The above value is then multiplied with i in range(1,terpolatedFrames) after which it is added to frame n.

An example video to show the interpolation will follow at a later stage.
