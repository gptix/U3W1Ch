import random


class Product:
    """
   Things that ACME sells.
   Each has:
   - name (string with no default)
   - price (integer with default value 10)
   - weight (integer with default value 20)
   - flammability (float with default value 0.5)
   -  identifier (integer, these are automatically genererated 
   (as a random (uniform) number from 1000000 to 9999999 (inclusive)).
   """
    # TODO:
    # - prevent negative prices
    # - prevent negative weights
    # - investigate legit ranges of prices, weights
    # - investigate legit range of flammabilities
    # - prevent re-use of ID numbers
    # - create function for making ID numbers, for ease of improvement later
    # - create variables to hold min and max for ID

    import random
    
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        """Create a new product object."""

        # Make like self.rating = int(rating)
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """
    calculates the price divided by the weight, and then returns a message: 
    - if the ratio is less than 0.5 return "Not so stealable...", 
    - if it is greater or equal to 0.5 but less than 1.0 return 
        "Kinda stealable.", and 
    - otherwise return "Very stealable!"
        """
        steal_score = self.price / self.weight
        if (steal_score < 0.5):
            return "Not so stealable..."
        elif (steal_score < 1.0):  # since we got here, we know it is >= 0.5
            return "Kinda stealable."
        else:                     # since we got here, we know it is >= 1.0
            return"Very stealable!"

    def explode(self):
        """
    calculates the flammability times the weight, and then returns a message:
     - if the product is less than 10 return "...fizzle.", 
     - if it is greater or equal to 10 but less than 50 return "...boom!", and 
     - otherwise return "...BABOOM!!
       """
        explosivity = self.flammability * self.weight
        if (explosivity < 10):
            return "...fizzle."
        elif (explosivity < 50):  # since we got here, we know it is >= 10
            return "...boom!"
        else:                     # since we got here, we know it is >= 50
            return "...BABOOM!!"


# Of course, Acme doesn't just sell generic products -
# it sells all sorts of special specific things!
# Make a subclass of Product named BoxingGlove that does the following:

class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        """
        Subclass of product.  Default weight is 10.  All other 
        defaults are the same as for Product.
        """
        super().__init__(name, price, weight, flammability)
        
    def explode(self):
        """Gloves don't explode."""
        return "...it's a glove."

    def punch(self):
        """
        Returns - "That tickles."  if the weight is below 5, 
                - "Hey that hurt!" if  weight is greater or equal to 5 
                                              but less than 15, and 
                - "OUCH!"          otherwise
        """
        
        if (self.weight < 5):
            return "Tht tickes."
        elif (self.weight < 15):
            return "Hey that hurt!"
        else:
            return "OUCH!"
