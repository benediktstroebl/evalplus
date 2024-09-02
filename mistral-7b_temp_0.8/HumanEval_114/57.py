import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums is None:
        return None
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    min_sum = 1000000
    for i in range(0,len(nums)):
        start_sum = 0
        for j in range(i, len(nums)):
            start_sum += nums[j]
            if start_sum < min_sum:
                min_sum = start_sum
    return min_sum

