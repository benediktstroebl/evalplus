

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
    
    # O(n) time
    # O(n) space
    # where n is the length of l

    # check if both elements is in l and have same value
    # • l[i] + l[j] == 0
    # • l[i] != l[j]
    # • l[i] not in l or l[j] not in l
    
    seen = set()
    for i in l:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False

assert pairs_sum_to_zero([]) == False
assert pairs_sum_to_zero([1]) == False
assert pairs_sum_to_zero([1, 3, 5, 0]) == False
assert pairs_sum_to_zero([1, 3, -2, 1]) == False
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6]) == False
assert pairs_sum_to_zero([-4, -2, 0, 3, 4, 5]) == True
assert pairs_sum_to_zero([2, -2, -3, 3, 3, 0]) == True
assert pairs_sum_to_zero([1, 1, 1, 1, 1, 1, 1]) == False
assert pairs_sum_to_zero([1, 1, 1, 1, 1, 1, 1, 1, 1]) == False