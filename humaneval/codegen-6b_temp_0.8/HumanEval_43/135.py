

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
    index_list = []
    for i in enumerate(l):
        for j in enumerate(l):
            if (i[0],j[0]) not in index_list:
                if i[1] == j[1]:
                    index_list.append((i[0],j[0]))
    if len(index_list) <2:
        return False
    else:
        return True

