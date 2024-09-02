

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
    # Your code here

    # use a hash table to keep track of elements
    # iterate through the list
    # if the element doesn't exist in the hash table,
    # add it to the hash table
    # iterate through the list again
    # if the element exists in the hash table,
    # return True
    # else return False

    # hash table to keep track of elements
    pair_dict = {}

    for num in l:
        if num in pair_dict:
            return True
        else:
            pair_dict[num] = 1

    return False
