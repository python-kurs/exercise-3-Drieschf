# Exercise 3

from pathlib import Path
import utils as ut
import csv

# import functions from utils here

data_dir = Path("data")
output_dir = Path("solution")

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]

cars_dir = Path(data_dir, "cars.txt")

# 2. Read the text file [2P]
    
cars=open(str(cars_dir), "r").read()

# 3. Count the occurences of each item in the text file [2P]

clist = list(cars.split("\n"))
occur = ut.countelem(clist)

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]

ut.dir_check(output_dir)

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...

counts = output_dir/"counts.csv"

with open(counts, "w") as file:
    writer = csv.DictWriter(file, fieldnames=["item", "count"]) 
    writer.writeheader()
    for key in occur.keys():
        file.write("%s,%s\n"%(key,occur[key])) 