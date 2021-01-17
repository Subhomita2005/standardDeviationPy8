import csv
with open("class2.csv",newline="" ) as f :
    reader=csv.reader(f)
    data=list(reader)
data.pop(0)
totalmarks=0
n=len(data)
for i in data:
    totalmarks+=float(i[1])
mean=totalmarks/n
print(mean)
import pandas as pd 
import plotly.express as px
df = pd.read_csv("class2.csv")
fig=px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[dict(type="line",y0=mean,y1=mean,x0=0,x1=n)])    
fig.show()