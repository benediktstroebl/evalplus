import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # brute force, O(n^3)
    # for i in range(0, len(nums)):
    #     for j in range(i, len(nums)):
    #         s = 0
    #         for k in range(i, j + 1):
    #             s += nums[k]
    #         if s < min:
    #             min = s
    # return min
    
    # dynamic programming, O(n^2)
    s = 0
    min = float("inf")
    for i in range(len(nums)):
        s += nums[i]
        if s < min:
            min = s
        if s < 0:
            s = 0

    return min if min!= float("inf") else 0
