
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # BEGIN SOLUTION
    # SORTED_LIST = []
    # # num_list = sorted(nums, key=lambda x: x, reverse=True)
    # for num in nums:
    #     sum = 0
    #     for i in num:
    #         sum += i
    #     # if num not in SORTED_LIST:
    #     SORTED_LIST.append((num, sum))
    #     # elif num in SORTED_LIST:
    #     #     SORTED_LIST.append((num, sum))
    # #     # SORTED_LIST.sort()
    # return SORTED_LIST
    # END SOLUTION
