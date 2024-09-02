

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

    # Add your code here
    if len(l) < 2:
        return False
    temp_dict = {}
    for i in l:
        if i not in temp_dict:
            temp_dict[i] = 1
        else:
            if 0 - i in temp_dict:
                return True
            else:
                temp_dict[i] += 1

    return False

