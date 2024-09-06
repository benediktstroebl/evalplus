

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """

    """
    First create two sets:
    1) one for positive numbers
    2) the other for negative numbers
    then return if there is any element in positive set such that the
    negative of that element is in the negative set
    """
    positive_numbers = set()
    negative_numbers = set()

    for i in l:
        if i > 0:
            positive_numbers.add(i)
        else:
            negative_numbers.add(i)

    return positive_numbers.intersection(negative_numbers)

