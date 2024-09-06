
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
    nums_copy = nums.copy()
    while len(nums_copy) != 0:
        num_with_max_points = max(nums_copy, key=sum_digit_points)
        result.append(nums_copy.pop(nums_copy.index(num_with_max_points)))
    return result

