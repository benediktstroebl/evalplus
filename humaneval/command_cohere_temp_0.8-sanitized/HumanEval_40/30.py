import unittest
def triples_sum_to_zero(lst):
    # Calculate total sum and count of list elements
    sum_ = sum(lst), len(lst)

    # Filter list of tuples where sum of three elements is zero
    triples = [(x, y, z) for x in lst for y in lst for z in lst if x + y + z == 0]

    # If there are three distinct elements that sum to zero, return True
    return bool(triples)