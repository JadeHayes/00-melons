"""Classes for melon orders."""
class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        # if country_code:
        #     self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == 'Christmas Melon':
                base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    # country_code = "US"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    # def __init__():
    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.country_code != 'US' and self.qty < 10:
            total += 3
        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """Calculates Government orders without tax and inspects melons"""
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        if passed:
            passed_inspection = True




order1 = DomesticMelonOrder("cantaloupe", 8)
order2 = DomesticMelonOrder("Christmas Melon", 8)
order3 = DomesticMelonOrder("Christmas Melon", 12)
order5 = InternationalMelonOrder("watermelon", 6, "AUS")
order6 = InternationalMelonOrder("watermelon", 12, "AUS")
order7 = GovernmentMelonOrder("cantaloupe", 8)