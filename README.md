# Stock Plotting - READ ME
This Python script produces plots from CSV files for stock trading.


## Requirements:
Python version 3.8.3
Libraries: pandas, matplotlib


## Updates

v1.0.2
Date: 2021-02-08-1007
1. Standard dataframe is normalized and then written to .csv file
2. Fixed bug so that Friday plots are normalized
3. Added directory folders for Input_CSV, Output_CSV, and Plotting

----------
v1.0.1
Date: 2021-02-07-2208
1. Added normalization. All stocks will begin at 100 in the plot.
2. Produces a new dataframe with Fridays only, and writes to .csv file
3. Produces a plot with Fridays only, and writes image to .png file
4. Fixed plot being cut off at the bottom

----------
v1.0.0
Date: 2021-01-25-1253
1. Double-click plotting.py to run the python script, which take all .csv files in the folder, plot charts, and write images to .png file.