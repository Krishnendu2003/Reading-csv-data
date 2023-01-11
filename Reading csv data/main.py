
# import csv
# with open("./weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         if row[1]!="temp":
#             temperature.append(int(row[1])) creating list of temperature
#
#
#
#     print(temperature)



import pandas as pd
# data=pd.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# convert whole data to a dictionry
# data_dict=data.to_dict()
# print(data_dict)
# print(data.temp) //getting a coloumn
# temp_list=data.temp.to_list()       #creating temp list
# print(temp_list)
# average=data.temp.mean()
# print(average)
# print(data.temp.max())
# get data of a row
# monday=data[data.day=="Monday"]
# print(monday)
# print(monday.condition)
# convert celcius to farenheit for monday temp
# print(int(monday.temp)*9/5+32)
# print the day which has heighest temp
# print(data[data.temp==data.temp.max()])

data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count=len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count=len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count=len(data[data["Primary Fur Color"] == "Black"])


data_dict={"Fur color":["Gray","Cinnamon","Black"],
           "Count":[grey_squirrel_count,cinnamon_squirrel_count,black_squirrel_count]}
dataframe=pd.DataFrame(data_dict)
dataframe.to_csv("Squirrel_count.csv")





