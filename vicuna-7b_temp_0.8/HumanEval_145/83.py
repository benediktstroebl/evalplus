
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
    digits = [0] * 10
    while nums:
        d = 0
        for num in nums:
            digit = sum(map(int, [str(num)]))
            digits[digit // 10] += digit % 10
        nums = [i for i in nums if i >= 0]
        nums.sort(key=lambda x: x if x >= 0 else -(digits[x // 10] + (x % 10)))
    return nums
