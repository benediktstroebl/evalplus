import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    min_sum = math.inf
    total_sum = 0
    for i in nums:
        total_sum += i
        if total_sum < min_sum:
            min_sum = total_sum
        if total_sum > 0:
            total_sum = 0
        if i < 0:
            total_sum += i

    if min_sum != math.inf:
        return min_sum
    return 0
