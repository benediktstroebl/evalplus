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
    elif len(nums) == 1:
        return nums[0]
    globalMin = math.inf
    total = 0
    n = len(nums)
    for i in range(n):
        total += nums[i]
        globalMin = min(globalMin, total)
        # print(total)
    return globalMin
