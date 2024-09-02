

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
    # A dictionary to keep track of the numbers we've seen
    seen = {}

    # Iterate through the list and add each number to the dictionary
    # If the complement of that number is in the dictionary, then return True
    for num in l:
        if num in seen:
            return True
        else:
            seen[num] = num

    # Iterate through again and subtract each number from 0 to
    # check if its complement is in the dictionary
    for num in l:
        if (0 - num) in seen:
            return True

    # if we got here then there are no pairs
    return False
