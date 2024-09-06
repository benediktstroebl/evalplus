

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
    set_of_nums = set()
    for number in l:
        if -number in set_of_nums:
            return True
        set_of_nums.add(number)
    return False
    # for index1, num1 in enumerate(l):
    #     for index2, num2 in enumerate(l):
    #         if index1 != index2 and num1 + num2 == 0:
    #             return True
    # print("Done")
    # return False

