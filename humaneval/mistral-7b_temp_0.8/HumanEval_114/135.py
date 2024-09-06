import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    current_sum = 0
    min_sum = math.inf
    l = len(nums)
    for i in range(l):
        current_sum += nums[i]
        min_sum = min(min_sum, current_sum)
        while i < l - 1 and current_sum > 0:
            current_sum -= nums[i]
            i += 1
            min_sum = min(min_sum, current_sum)
    if min_sum == math.inf:
        min_sum = 0
    return min_sum
