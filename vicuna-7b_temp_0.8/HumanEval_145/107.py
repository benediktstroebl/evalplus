
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
    # sort the list and then find the indices of elements whose sum of digits
    # is greater than the index of the current element
    sorted_nums = sorted(nums)
    return [nums[i] for i, num in enumerate(sorted_nums) if num % 10 > sorted_nums[i] % 10]
