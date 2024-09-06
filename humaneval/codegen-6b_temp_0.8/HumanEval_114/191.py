import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    """
    Explanation:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    1) subarray_sum = -6
    2) subarray_sum = -5 + (-6(1) + (-3) + (-1(2)) + 4 + 1 + (2) + 1 + (5))
    3) subarray_sum = -5 + (-6(1) + (-3) + (-1(2)) + 4 + 1 + (2) + 1 + (-5))
    4) subarray_sum = -5 + (-6(1) + (-3) + (-1(2)) + 4 + 1 + (2) + (1) + (-5))
    5) subarray_sum = -5 + (-6(1) + (-3) + (-1(2)) + 4 + 1 + (2) + 1(1) + (-5))

    Since nums[5] - nums[1] = -1, we have our minSum = -6

    """
    total = 0
    smallest = math.inf
    for i, num in enumerate(nums):
        total += num
        smallest = min(smallest, total)
        if total == 0:
            break
    return smallest

