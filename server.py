from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

from cupcakes import view_all_cupcakes, add_cupcake_csv, find_cupcake, convert_cupcake_dict

def order_total(file):
    order = view_all_cupcakes(file)
    return round(sum([float(x["price"]) for x in order]), 2)

@app.route('/')
def home():
    cupcakes = view_all_cupcakes('cupcakes.csv')
    return render_template('index.html', cupcakes=cupcakes, order_total=order_total('orders.csv'))

@app.route('/orders')
def orders_page():
    cupcakes = view_all_cupcakes('orders.csv')
    return render_template('order.html', cupcakes=cupcakes, order_total=order_total('orders.csv'))

@app.route('/add-cupcake/<name>')
def add_cupcake(name):
    cupcake_dict = find_cupcake('cupcakes.csv', name)
    cupcake = convert_cupcake_dict(cupcake_dict)
    add_cupcake_csv('orders.csv', cupcake)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.env = 'development'
    app.run(debug = True, port = 4321, host = 'localhost')