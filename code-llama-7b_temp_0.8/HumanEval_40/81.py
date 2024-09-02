

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
    # dictionary to store the sum and its count of elements which sum to it
    triples = dict()
    # iterate through all elements and calculate its sum
    for element in l:
        sum_val = 0 - element
        if sum_val in triples:
            triples[sum_val] += 1
            if triples[sum_val] > 2:
                return True
        else:
            triples[sum_val] = 1
    return False

