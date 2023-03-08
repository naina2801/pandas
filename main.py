import pandas as pd
import openpyxl
#Series

# l = [1,2,3,4,5]
# ser = pd.Series(l)
# print(ser)
# print(ser.iloc[2])

#DataFrame

# data = {
#     "name" : ["Nm","As","Na"],
#     "age" : [22,33,43],
#     "id" : [101,102,103]
# }
# dt = pd.DataFrame(data)
# print(dt)
# print(dt.iloc[1,2])
# print(dt.iloc[1,1])
# print(dt.iloc[2,:])


# df = pd.read_csv(r'sample.csv', encoding= 'unicode_escape')
# print(df)

# toxl = pd.read_csv("phonecsv.csv").to_json("phonejson.json")
# print(toxl)
# #
# json_file = {'name':["aparna", "pankaj", "sudhir", "Geeku"],'degree': ["MBA", "BCA", "M.Tech", "MBA"],'score':[90, 40, 80, 98]}
# df = pd.DataFrame(json_file).to_csv("exce.csv")
# print(json_file)
# print(df)

# dt = pandas.DataFrame("animal.json").to_excel("animal.xlsx")
# print(dt)
df=pd.read_csv("phonecsv.csv")
# print(df.head(6))
# print(df.iloc[5,7])
# print(df.iloc[5,6])
# print(df.tail(6))
# print(df["name"])
# print(df.info())
# print(df.fillna(12345678,inplace=True))
replacevalue = df.loc[16,"price"] = 280120
print(replacevalue)
print(df.to_string())
print(df.duplicated())
print(df.corr())

# df = pd.to_excel("data.xlsx")
# print(df.to_string())