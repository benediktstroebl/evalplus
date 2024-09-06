

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
    # hash table for storing the values.
    # key is the value of the input, value is the index of the input
    # (to be able to lookup the other value)
    hash_table = {}

    for i in range(len(l)):
        # get the value at the current index
        current_value = l[i]
        # get the value from the hash table
        other_value = hash_table.get(current_value)
        # check to see if we have a value in our hash table
        if other_value is not None:
            # we have a value, check if it is the current index or the other
            # index
            if other_value != i:
                # we have two distinct values, return true
                return True
        # we don't have a value, add the current index to the hash table.
        # the key is the current value, and the value is the current index
        hash_table[current_value] = i

    # if we haven't returned, we don't have a pair of distinct values that sum
    # to zero
    return False

