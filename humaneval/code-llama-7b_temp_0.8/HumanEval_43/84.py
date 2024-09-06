

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
    if len(l) == 1:
        return False

    # sort the list so we can use two pointers to find the pair
    l.sort()
    for i in range(len(l) - 1):
        # we want to make sure we don't get the same number twice
        if i > 0 and l[i] == l[i - 1]:
            continue

        # the pointers start at the extremes and move towards the middle
        left = i
        right = len(l) - 1

        # this is the sum of the two integers
        total = l[left] + l[right]

        # we want the two numbers to sum to zero
        if total == 0:
            return True
        elif total < 0:
            # we want to keep the pointers from getting too close together
            # if we sum to a positive number, we know that the other number
            # will be negative, and that there is no chance of a sum to zero
            left += 1
        else:
            right -= 1

    # if the function does not return, then there is no pair that sums to zero
    return False

