

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
    # TODO: Write your code here

    # list_sorted = sorted(l)
    # temp = 0
    # for i in range(0, len(list_sorted)):
    #     for j in range(i+1, len(list_sorted)):
    #         temp = list_sorted[i]+list_sorted[j]
    #         if temp == 0:
    #             return True
    # return False

    return sorted(set(l) - set([0])) == sorted(set(l) - set([0]))

