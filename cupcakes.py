import csv

def write_new_csv(file):
  with open(file, 'w') as csvfile:
    fieldnames = ["size", "name", "price", "flavor", "frosting", 'filling', 'sprinkles']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()

class Cupcake:
  size = 'regular'
  def __init__(self, name, price, flavor, frosting, filling, sprinkles):
    self.name = name
    self.price = price
    self.flavor = flavor
    self.frosting = frosting
    self.filling = filling
    self.sprinkles = sprinkles

class Regular(Cupcake):
  size = 'regular'

class Mini(Cupcake):
  size = 'mini'

class Large(Cupcake):
  size = 'large'

def add_cupcake_csv(file, cupcake):
  with open(file, 'a', newline='\n') as csvfile:
    fieldnames = ["size", "name", "price", "flavor", "frosting", 'filling', 'sprinkles']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})

def convert_cupcake_dict(cupcake):
  return Cupcake(cupcake['name'], cupcake['price'], cupcake['flavor'], cupcake['frosting'], cupcake['filling'], cupcake['sprinkles'])


def view_all_cupcakes(file):
  with open(file) as csv_file:
    reader = csv.DictReader(csv_file)
    reader = list(reader)
    return reader
  
def find_cupcake(file, name):
  for cupcake in view_all_cupcakes(file):
    if cupcake['name'] == name:
      return cupcake
  return None

cupcake1 = Regular('Stars and Stripes', 2.99, 'Vanilla', 'Vanilla', 'Chocolate', 'Red White and Blue')
cupcake2 = Regular('Oreo', 1.99, 'Chocolate', 'Cookies and Cream', 'Cookies and Cream', 'Chocolate')
cupcake3 = Mini('Red Velvet', 3.99, 'Red Velvet', 'Cream Cheese', 'Cream Cheese', None)
cupcake4 = Large('Chocolate Supreme', 2.99, 'Chocolate', 'Chocolate', 'Chocolate', 'Chocolate')
cupcake5 = Mini('Strawberry Delight', 1.99, 'Strawberry', 'Vanilla', 'Chocolate', 'Strawberry')
cupcake6 = Large('Boring Vanilla', 1.99, 'Vanilla', 'Vanilla', 'Vanilla', 'Vanilla')


cupcakes = [
  cupcake1,
  cupcake2,
  cupcake3,
  cupcake4,
  cupcake5,
  cupcake6
]