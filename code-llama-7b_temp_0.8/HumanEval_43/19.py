

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

    # create a dictionary that will hold as keys, each element of the list
    # and as values the number of occurrences of that element in the list.
    occurrences = dict()
    for element in l:
        occurrences[element] = occurrences.get(element, 0) + 1

    # go through the dictionary and check if there is a key whose value is 2.
    # if there is, we found a pair whose sum is 0.
    for key, value in occurrences.items():
        if value == 2:
            return True

    # if there is no key whose value is 2, return False.
    return False

