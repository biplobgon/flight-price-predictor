```python
from flask import Flask
render_template
import pandas as pd

app = Flask (_name_)
@app.route('/')
def index():
  daily_data = pd.read_csv('flights_data.csv')
  cheapest_route = find_cheapest_route(daily_data)
  return render_template('index.html', route = cheapest_route)

def find_cheapest_route(df):
  cheapest = df.loc[df['price'].idxmin()]
  return cheapest

if __name__ =='__main__':
  app.run(debug = True)
