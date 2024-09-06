import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    else:
        minsum = math.inf
        s = 0
        for x in nums:
            if s > 0:
                s += x
            else:
                s = x
            if s < minsum:
                minsum = s
        return minsum

