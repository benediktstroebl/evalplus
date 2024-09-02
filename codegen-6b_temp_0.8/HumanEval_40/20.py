

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    count = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            if i != j and l[i] + l[j] == 0:
                count += 1

    if count == 3:
        return True
    else:
        return False

assert triples_sum_to_zero([1, 3, 5, 0]) == False
assert triples_sum_to_zero([1, 3, -2, 1]) == True
assert triples_sum_to_zero([1, 2, 3, 7]) == False
assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
assert triples_sum_to_zero([1]) == False

"""
Extra Credit:

Write a function that takes a list of numbers and returns the
entries that are positive, negative, or zero, in ascending order.

Hint: Use a loop and the function `list`, `len`, `sum`, `max`, `min`

>>> positives([4, -1, 0, 6, 10])
[4, 6, 10]
>>> negatives([-4, 1, 0, -6, 10])
[-4, -6, -10]
"""
