import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    cum_sum = 0
    cum_sum_min = math.inf
    start = 0
    for i, num in enumerate(nums):
        cum_sum += num
        while cum_sum < cum_sum_min and i - start > 0:
            cum_sum -= nums[start]
            start += 1
        if cum_sum < cum_sum_min:
            cum_sum_min = cum_sum
    return cum_sum_min
