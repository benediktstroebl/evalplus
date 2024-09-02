

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
    for x in l:
        for y in l:
            if x + y == 0:
                return True
        if l[-1] != l[0]:
            return True
    return False

test = [1, 2, 3, 4, 0, 5, 6, -1, 8, -2, 3, -3, 4]
for i in test:
    print(f"{i} {pairs_sum_to_zero(test)}")