from collections import OrderedDict  # to sort dictionaries

#Importing Printable class, then pass it to Transaction class for inheritence
from utility.printable import Printable


class Transaction(Printable):
    def __init__(self, sender, recipient, amount, signature):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature


   
    def to_ordered_dict(self):
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])
