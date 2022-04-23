import pandas as pd
import os, math, time

# 160353103 rows with ending
# 160033094 rows w/o pixel ending
# 320010 pixles placed during ending

start_time = time.time()

os.system ('cls' if os.name == 'nt' else 'clear')

filename = "SortedSet.csv"

data = pd.read_csv(filename)

time = (time.time() - start_time)
print(f"{time} seconds to load")
print(f"~{math.floor(time / 60)} minutes to load")

Count = 0
Color = '\"FFFFFF\"'
Cords = "0,0"

#data.to_csv("TimeSortedSet2.csv", index=False)

for r in range (len(data.index)):
    if data.coordinate[r] == Cords:
        if data.pixel_color[r] == Color:
            #print(f"line {r+1}, and {r+2}")
            Count += 1
            Color = data.pixel_color[r]
        else:
            Color = data.pixel_color[r]
    else:
        Cords = data.coordinate[r]
        Color = data.pixel_color[r]

time = (time.time() - start_time)
print(f"{time} seconds to finish")
print(f"{math.floor(time / 60)} minutes to finish")

print(f"Count: {Count}")
print(f"Time: {Count * 5} minutes")
