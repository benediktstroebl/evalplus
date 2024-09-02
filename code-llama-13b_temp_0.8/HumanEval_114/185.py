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
    if len(nums) == 1:
        return nums[0]
    minSum = math.inf
    left = 0
    right = 1
    while right < len(nums):
        current = sum(nums[left:right])
        if minSum > current:
            minSum = current
        left += 1
        right += 1
    return minSum
