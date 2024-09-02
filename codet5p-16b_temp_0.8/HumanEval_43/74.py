

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

    dict_l = {}
    for i in l:
        if i not in dict_l:
            dict_l[i] = 1
        else:
            dict_l[i] = dict_l[i] + 1

    for i in l:
        if dict_l[i] > 1:
            if i == 0:
                if dict_l[0] >= 2:
                    return True
            else:
                if i*i == 0:
                    return True
                else:
                    if i in dict_l and (i*i) in dict_l:
                        return True

    return False


