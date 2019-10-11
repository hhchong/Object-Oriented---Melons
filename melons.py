"""Classes for melon orders."""
class AbstractMelonOrder():

    def __init__(self, species, qty, order_type):

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas":
            base_price = base_price * 1.5 

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            return total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic")

    
    tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):

    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international")

        self.country_code = country_code


    tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super().__init__(species, qty, "government")

        self.passed_inspection = False


    tax = 0 


    def mark_inspection(self, passed):

        
        self.passed_inspection = passed









