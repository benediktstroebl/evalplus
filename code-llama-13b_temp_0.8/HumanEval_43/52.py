

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

    # create an empty dictionary
    d = {}

    # iterate over every element in the list
    for elem in l:
        # check if the complement of the element is already in the dictionary
        if elem in d:
            return True

        # if it is not, add the elem and its complement to the dictionary
        else:
            d[elem] = 0

    return False

