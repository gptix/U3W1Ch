import random
"""generate random products and print a summary of them. 
Only use the Product class."""

# TODO - make ths a class or two

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
MIN_PRICE = 5
MAX_PRICE = 100
MIN_WEIGHT = 5
MAX_WEIGHT = 100
MIN_FLAM = 0
MAX_FLAM = 2.5

# The below are used to generate random numbers as indices to lists.
index_last_adj = len(ADJECTIVES) - 1
index_last_noun = len(nons) - 1

def random_name():
  adj = adjectives[random.randint(1,index_last_adj)]
  noun = nouns[random.randint(1,index_last_noun)]
  return (adj + " " + noun)

def random_price():
  return random.randint(MIN_PRICE, MAX_PRICE)

def random_weight():
  return random.randint(MIN_WEIGHT,MAX_WEIGHT)

def random_flammability():
  return (random.uniform(MIN_FLAM, MAX_FLAM))

def random_product():
  n = random_name()
  p = random_price()
  w = random_weight()
  f = random_flammability()
  # return n, p, w, f
  return Product(n, p, w, f)

def generate_products(n=30):
    """Generate a given number of products (default 30), 
    randomly, and return them as a list. 
    For the purposes of generation, "random" means uniform 
    - all possible values should vary uniformly across the 
    following possibilities:

    name should be a random adjective from ['Awesome', 
    'Shiny', 'Impressive', 'Portable', 'Improved'] 
    followed by a space and then a random noun from ['Anvil', 
    'Catapult' 'Disguise' 'Mousetrap', '???'], 
    e.g. 'Awesome Anvil' and Portable Catapult' are both possible
    price and weight should both be from 5 to 100 (inclusive and 
    independent, and remember - they're integers!)
    flammability should be from 0.0 to 2.5 (floats)
    """
    # TODO: make sure input is a postive integer.
    
def generate_products(num_products=30):
    products = [random_product() for i in range(num_products)]
    return products
    # return [random_product() for i in range(num_products)]



def inventory_report(products):

    import pandas as pd
    """
    Takes a list of products, and prints a "nice" summary.
    """
    prod_count = len(products)

    prices = []
    weights =[]
    flams = []
    names = []
    for i in range(prod_count):
      p = products[i]
      prices.append(p.price)
      weights.append(p.weight)
      flams.append(p.flammability)
      names.append(p.name)
    
    d = {'Name': names, 'Price': prices, 'Weight' : weights, 'Flammability' : flams}
    prod_df = pd.DataFrame(data = d)
    print("Nice Summary Product Report")
    print(f"Product Count: {prod_count}")
    return (print(prod_df.describe()))
