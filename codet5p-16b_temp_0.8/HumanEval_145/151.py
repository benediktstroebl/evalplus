
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

    nums_list = nums[:]
    sorted_nums = []

    while len(nums_list)!= 0:
        min_index = None
        for i in range(len(nums_list)):
            if min_index is None:
                min_index = i
                continue

            if sum_of_digits(nums_list[min_index]) > sum_of_digits(nums_list[i]):
                min_index = i
        sorted_nums.append(nums_list[min_index])
        nums_list.remove(nums_list[min_index])

    return sorted_nums

