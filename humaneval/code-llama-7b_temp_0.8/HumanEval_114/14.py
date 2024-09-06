import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total = 0
    minSub = math.inf
    for num in nums:
        total += num
        if total < minSub:
            minSub = total
        if total < 0:
            total = 0
    if minSub == math.inf:
        return 0
    else:
        return minSub
