import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    
    sums = [0] * (len(nums) + 1)
    for i in xrange(len(nums)):
        sums[i + 1] = sums[i] + nums[i]

    min_sum = sums[len(sums) - 1]
    for i in xrange(len(sums) - 2, -1, -1):
        if sums[i] >= 0:
            min_sum = min(min_sum, sums[len(sums) - 1] - sums[i])

    return min_sum

