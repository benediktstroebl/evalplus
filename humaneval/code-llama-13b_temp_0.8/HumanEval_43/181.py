

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
    # copy the list
    l_copy = l[:]
    # sort the list
    l_copy.sort()
    # get the length of the list
    l_copy_length = len(l_copy)
    # initialize a variable to hold the index of a first element
    i = 0
    # iterate through the sorted list
    while i < l_copy_length:
        # initialize a variable to hold the index of a second element
        j = i + 1
        # iterate through the sorted list, starting from the second element
        while j < l_copy_length:
            # if the sum of the two elements is equal to zero, return True
            if l_copy[i] + l_copy[j] == 0:
                return True
            # otherwise, increment the index of the second element
            j += 1
        # increment the index of the first element
        i += 1
    # return False
    return False
