

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

    if not len(l):
        return False
    elif len(l)==1:
        return False
    else:
        index_1 = 0
        index_2 = 1
        while index_1<len(l):
            while index_2<len(l):
                if l[index_1]+l[index_2]==0:
                    return True
                index_2+=1
            index_2=0
            index_1+=1
        return False
