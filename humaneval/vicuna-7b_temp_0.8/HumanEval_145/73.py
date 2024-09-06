
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
    nums = as_tuple(nums)
    n = len(nums)
    if n == 0:
        return []
    result = []
    for i in range(n):
        for j in range(i+1, n):
            digit_sum = sum([digit * (i // (j // (digit - 1))) for digit in str(nums[j])])
            if digit_sum == abs(nums[i]):
                result.insert(0, nums[i])
                break
            elif digit_sum > abs(nums[i]):
                result.insert(0, nums[j])
            else:
                result.insert(0, nums[i])
    return result
