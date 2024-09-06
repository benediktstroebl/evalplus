

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
    # list_of_zeros = [0]
    # lst = list_of_zeros.extend(l)
    # l.extend(list_of_zeros)
    # l.sort()
    # for i in range(0, len(l)):
    #     if l[i] == l[i+1]:
    #         return False
    #     else:
    #         if l[i] + l[i+1] == 0:
    #             return True
    #         else:
    #             continue
    # return False

    # l1 = l.copy()
    # for i in l1:
    #     l.remove(i)
    #     if -i in l:
    #         return True
    # return False

    l1 = set(l)
    for i in l1:
        if (-i) in l1:
            return True
    return False

