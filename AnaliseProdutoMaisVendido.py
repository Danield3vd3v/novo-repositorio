import pandas as pd
import plotly.express as px

dff = []

for df in pd.read_csv('Iowa_Liquor_Sales.csv', chunksize=1000000):

    f = df.groupby('Item Description').sum()
    dff.append(f)

h = pd.DataFrame(columns=['Store Number','County Number','Category','Vendor Number','Item Number','Pack','Bottle Volume (ml)','Bottles Sold','Volume Sold (Liters)','Volume Sold (Gallons)'])

for df in dff:
    h = pd.concat([h, df])

h['Products'] = h.index

h = h.sort_values(by='Bottles Sold', ascending=False)#.groupby('Products').sum()#

h['Bottles Sold'] = h['Bottles Sold'].astype('int')

c = h.groupby('Products').sum().sort_values(by='Bottles Sold', ascending=False)

o = c.head(20)
fig = px.bar(o, x=o.index, y='Bottles Sold', labels={'x':'Produtos', 'Bottles Sold': 'Número de Garrafas vendidas'})
fig.show()


