import os
import glob
import pandas as pd
import matplotlib.pyplot as plt


from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

def normalize(df):
    stocks = df.iloc[:, 1:]
    initial = df.iloc[0, 1:]
    df.iloc[:, 1:] = stocks.div(initial, axis='columns')*100
    return df

def timefilter(df):
    df["dayint"] = df.iloc[:, 0].dt.dayofweek
    df = df[df.dayint == 4]
    df = df.drop("dayint", axis = 1)
    return df


dir_path = os.path.dirname(os.path.realpath(__file__))
input_CSV_path = os.path.join(dir_path, "Input_CSV")
output_CSV_path = os.path.join(dir_path, "Output_CSV")
plotting_path = os.path.join(dir_path, "Plotting")

os.chdir(input_CSV_path)
csvlist = [f for f in glob.glob("*.csv")]

for csvfile in csvlist:
    name = csvfile.split(".csv")
    name = name[0]

    os.chdir(input_CSV_path)
    data = pd.read_csv(csvfile, parse_dates = ["Date"])
    
    data = normalize(data)
    name += "_norm"

    
    os.chdir(plotting_path)
    data.plot(x = "Date", title = name)
    plt.savefig(name + ".png")
    
    os.chdir(output_CSV_path)
    cfname = name + ".csv"
    data.to_csv(cfname, index = False)

    # timefilter to fridays only
    data = timefilter(data)
    if data.size != 0:
        data = normalize(data)

        os.chdir(plotting_path)
        name += "_fri"
        data.plot(x = "Date", title = name)
        plt.savefig(name + ".png")

        os.chdir(output_CSV_path)
        cfname = name + ".csv"
        data.to_csv(cfname, index = False)
