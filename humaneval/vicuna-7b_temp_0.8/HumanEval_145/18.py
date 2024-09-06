
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
    nums = sorted(nums)
    if nums == []:
        return []
    while nums:
        num = nums.pop(0)
        digits = sum([int(n) for n in str(num)])
        if digits >= 1000:
            # We can use a temporary variable to store the next number
            # without affecting the original list.
            nums.append(num + str(digits % 10))
            digits = int(digits / 10)
        else:
            nums.append(num + str(digits))
        digits = int(digits)
    return nums
