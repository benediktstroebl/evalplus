

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
    # list of numbers that sum to zero
    num_list = [num for num in l if num == 0]
    # list of numbers that don't sum to zero
    num_list1 = [num for num in l if num != 0]
    # list of sums between each number and zero
    num_list2 = [abs(num) for num in l]

    # if there is no number in list that sums to zero
    if len(num_list) == 0:
        # return false
        return False

    # if there is a number in list that sums to zero
    if len(num_list) >= 1:
        # return true
        return True

    # if there is a number in list that doesn't sum to zero
    if len(num_list1) >= 1:
        # set the list of sums to 0
        num_list2 = [0]
        # return true if there is a number in num_list2
        return num_list2[0] in num_list1




