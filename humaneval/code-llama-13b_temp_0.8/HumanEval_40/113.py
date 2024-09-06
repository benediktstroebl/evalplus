

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
    # Remember to include the base case!
    if len(l) < 3:
        return False

    # TODO: write a for loop here to check if there are three elements in l that sum to zero
    # 1. Get the first element
    # 2. Check if the sum of the first element and the sum of any two of the other elements in the list
    #    is 0.
    #   2a. If the sum is 0, return True.

    # TODO: write the rest of the function



