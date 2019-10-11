"""Classes for melon orders."""
class AbstractMelonOrder:

    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price + self.flat_fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    # order_type = "domestic"
    tax = 0.08
    flat_fee = 0


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17

    if qty < 10:
        flat_fee = 3
    else:
        flat_fee = 0
    # order_type = "international"


    def __init__(self, country_code):
        """Initialize melon order attributes."""

        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
