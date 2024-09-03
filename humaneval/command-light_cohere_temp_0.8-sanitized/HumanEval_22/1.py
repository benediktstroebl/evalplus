from typing import List
def filter_integers(values):
    return [int(el) for el in values if type(el) == int]