

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
    # find the first negative integer in the list
    first_negative = -1
    for i in l:
        if i < 0:
            first_negative = l.index(i)
            break
        first_negative = -1

    # if there are no negative integers, return True
    if first_negative == -1:
        return True

    # find the second negative integer in the list
    second_negative = -1
    for i in l[first_negative + 1:]:
        if i < 0:
            second_negative = l.index(i)
            break

    # if the first negative integer and the second negative integer
    # is the same, return False
    if first_negative == second_negative:
        return False

    # else, return True
    return True

