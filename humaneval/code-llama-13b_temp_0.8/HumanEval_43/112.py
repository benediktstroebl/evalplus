

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
    # total=0
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         total = l[i] + l[j]
    #         if total == 0:
    #             return True
    # return False

    # if len(l) < 2:
    #     return False
    # for i in l:
    #     if 0 - i in l:
    #         return True
    # return False

    # Checking for odd length list
    if len(l) % 2 != 0:
        return False
    # Creating a set of elements of list
    my_set = set(l)
    # Iterating over elements of set
    for i in my_set:
        # If 0-x is in set, we found a pair that sums to zero
        if 0 - i in my_set:
            return True
    # If we reach here, then no pair was found
    return False

