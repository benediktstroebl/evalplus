

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
    # check for empty list
    if l == []:
        return False

    # create a set of already seen elements
    seen = set()
    # loop through each element in the list
    for element in l:
        # if element is already seen, return True
        if element in seen:
            return True
        # otherwise, add element to the set
        else:
            seen.add(element)

    # if there are no pairs, return False
    return False
