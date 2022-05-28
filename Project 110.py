import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
data = pd.read_csv("medium_data.csv")
data = data["reading_time"].tolist()
mean = st.mean(data)
stdev = st.stdev(data)
fig = ff.create_distplot([data],["reading_time"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1], mode ="lines",name = "MEAN"))
fig.show()
print(mean)
print(stdev)
dataset = []
for i in range(0,100):
    randomindex = random.randint(0,len(data))
    value = data[randomindex]
    dataset.append(value)
mean = st.mean(dataset)
stdev = st.stdev(dataset)
print(mean)
print(stdev)
