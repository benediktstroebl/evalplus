

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
    # make a dictionary to store the count of each number
    # if key is the number, value is the number of times it appeared
    # if key is zero, value is 1
    num_to_count = {}
    for num in l:
        if num in num_to_count:
            num_to_count[num] += 1
        else:
            num_to_count[num] = 1

    for num in l:
        if -num in num_to_count:
            if num_to_count[-num] >= 2:
                return True

    return False
