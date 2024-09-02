

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

    l2 = l.copy()
    l2.sort()

    for i in range(len(l2) - 1):
        # skips the elements with the same values
        if i > 0 and l2[i] == l2[i - 1]:
            continue

        j = i + 1
        while j < len(l2):
            if l2[i] + l2[j] == 0:
                return True
            if l2[i] + l2[j] > 0:
                break

            j += 1

    return False

