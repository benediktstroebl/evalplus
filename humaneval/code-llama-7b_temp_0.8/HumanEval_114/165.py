import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # s = sum(nums)
    # minSub = s
    # for i in range(len(nums)):
    #     s -= nums[i]
    #     if s < minSub:
    #         minSub = s
    # return minSub
    if not nums:
        return 0
    minSub = nums[0]
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        if s < minSub:
            minSub = s
    return minSub
