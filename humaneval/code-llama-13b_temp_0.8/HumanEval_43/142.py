

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
    # make a list of all possible sums
    # for example, for [1, 2, 3], we will get [3, 4, 5]
    possible_sums = []
    for n in l:
        possible_sums.append(n + 0)
        possible_sums.append(n + 1)
        possible_sums.append(n + 2)

    # make a new list with only the unique values
    unique_possible_sums = []
    for n in possible_sums:
        if n not in unique_possible_sums:
            unique_possible_sums.append(n)

    # check if there is 0
    if 0 in unique_possible_sums:
        return True

    # for each item in the list, check if its opposite is in the list
    for n in l:
        if (-n) in l:
            return True

    # if we get to this point, there are no pairs
    return False





