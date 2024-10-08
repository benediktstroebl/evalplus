
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
    digits.sort()
    return [nums[i] for i in range(n) if int(str(nums[i])) in digits for nums in nums]

