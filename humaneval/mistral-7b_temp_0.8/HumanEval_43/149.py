

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
    my_dict = {}
    for i in l:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    if l.count(0) == 1:
        return True
    for key in my_dict:
        if key == 0:
            continue
        if my_dict[key] == 0:
            continue
        if my_dict.get(key + 0, 0) > 0:
            return True
    return False

