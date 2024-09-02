import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # brute force
    if nums is None or len(nums) == 0:
        return 0
    min_sum = math.inf
    for i in xrange(0, len(nums)):
        sum = 0
        for j in xrange(i, len(nums)):
            sum += nums[j]
            min_sum = min(min_sum, sum)
    return min_sum
