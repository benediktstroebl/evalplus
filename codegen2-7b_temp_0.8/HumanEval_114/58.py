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
    if len(nums) == 1:
        return nums[0]

    n = nums[0]
    res = n
    for i in range(1, len(nums)):
        n += nums[i]
        res = min(res, n)
        if res < n:
            n = n - nums[i]

    
