
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

    result = []
    sum = []
    for num in nums:
        sum.append(sum_of_digits(num))
    for _ in range(len(nums)):
        min_ = min(sum)
        min_index = sum.index(min_)
        result.append(nums[min_index])
        del nums[min_index]
        del sum[min_index]

    return result
