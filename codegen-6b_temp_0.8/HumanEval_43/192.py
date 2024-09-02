

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
    return (len(l)>2) and (sum(l) == 0) and not check_duplicates(l)

l2 = [1,3,5,7]
assert pairs_sum_to_zero(l2)

l3 = [-5,3,5,7, -10]
assert pairs_sum_to_zero(l3)

l4 = [-5, 3, 5, 7]
assert not pairs_sum_to_zero(l4)

l5 = [1, -3, 5, 7, -10]
assert not pairs_sum_to_zero(l5)

l6 = [1, 3, 5, 7]
assert not pairs_sum_to_zero(l6)

l7 = []
assert not pairs_sum_to_zero(l7)

