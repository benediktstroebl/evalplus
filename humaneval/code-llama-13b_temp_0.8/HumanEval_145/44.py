
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
    #pass
    nums_sum = [sum(map(int, list(str(num)))) for num in nums]
    nums_sum_index = list(zip(nums_sum, nums))
    nums_sum_index.sort()
    nums_index = [num for (key, num) in nums_sum_index]
    return nums_index

