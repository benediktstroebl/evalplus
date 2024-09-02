

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
    positive_negative = {num for num in l if num < 0}
    sum_of_two_different_numbers = {abs(num) for num in l if abs(num) != num}
    if len(positive_negative) == len(sum_of_two_different_numbers):
        if sum(positive_negative) == 0:
            return True
        return False
    return False

