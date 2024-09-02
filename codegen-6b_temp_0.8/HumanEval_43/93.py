

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
    # HINT: Think of this solution using two pointers

    sorted_list = sorted(l)
    left_pointer = 0
    right_pointer = len(l) - 1

    while left_pointer < right_pointer:
        left_val = sorted_list[left_pointer]
        right_val = sorted_list[right_pointer]
        if left_val + right_val == 0:
            return True
        elif left_val + right_val < 0:
            left_pointer += 1
        else:
            right_pointer -= 1

    return False

