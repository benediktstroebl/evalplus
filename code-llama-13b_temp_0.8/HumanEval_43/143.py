

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
    zero_count = 0
    i = 0
    while i < len(l) and zero_count < 2:
        if l[i] == 0:
            zero_count += 1
        else:
            j = i + 1
            while j < len(l) and zero_count < 2:
                if l[j] == 0:
                    zero_count += 1
                    if zero_count == 2:
                        return True
                else:
                    if 0 - l[i] == l[j]:
                        return True
                j += 1
        i += 1
    return False
