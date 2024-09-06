

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
    # hint: the best way to solve this problem is to make two passes
    # through the list, and for each element e, check if -(e) is in the list.

    # best way is using a set
    seen = set()
    for i in l:
        if -(i) in seen:
            return True
        seen.add(i)
    return False

    # the worst way is using two for loops
    # for i in range(len(l)):
    #     for j in range(len(l)):
    #         if l[i] + l[j] == 0:
    #             return True
    # return False

