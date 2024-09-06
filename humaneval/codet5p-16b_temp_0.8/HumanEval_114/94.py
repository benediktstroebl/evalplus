import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if not nums: return 0
    
    numsLen = len(nums)
    s = 0
    minSum = math.inf
    for i in range(numsLen):
        s += nums[i]
        if minSum > s:
            minSum = s
        if s >= 0:
            continue
        for j in range(i, numsLen):
            s += nums[j]
            if minSum > s:
                minSum = s
            if s >= 0:
                break
    return minSum

