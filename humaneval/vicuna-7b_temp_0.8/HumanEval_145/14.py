
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
    n = len(nums)
    if n == 0:
        return []
    digits = [sum(int(d) for d in str(num)) for num in nums]
    if n == 1:
        return digits[0]
    else:
        indices = [i for i, d in enumerate(digits) if d >= digits[0]]
        return [nums[i] for i in indices]
