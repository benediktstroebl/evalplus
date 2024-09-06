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
    minsum = nums[0]
    sum = 0
    for num in nums:
        sum += num
        if sum < 0:
            sum = 0
        if sum < minsum:
            minsum = sum
    return minsum
