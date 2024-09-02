

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
    # 1. take a sorted list of distinct numbers
    # 2. start with the first and last elements
    # 3. if they sum to 0, return True
    # 4. if they are the same, return False
    # 5. if they sum to less than 0, move the first index to the right
    # 6. if they sum to more than 0, move the last index to the left
    # 7. return False

    # if there are fewer than 2 elements, return False
    if len(l) < 2:
        return False

    # sort the list
    l = sorted(l)

    # start first index and last index at 0
    first_index = 0
    last_index = len(l) - 1

    # check if the first and last numbers sum to zero
    if l[first_index] + l[last_index] == 0:
        return True

    # if the first and last numbers are the same, return False
    if l[first_index] == l[last_index]:
        return False

    # if the sum of the first and last numbers is negative, move the first
    # index to the right
    if l[first_index] + l[last_index] < 0:
        first_index += 1
    # if the sum of the first and last numbers is positive, move the last index
    # to the left
    else:
        last_index -= 1

    # return False
    return False


