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
    minSubArraySum = nums[0]
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    for i in range(1, len(nums)):
        if nums[i] < minSubArraySum:
            minSubArraySum = nums[i]
        elif nums[i] - nums[i - 1] < minSubArraySum:
            minSubArraySum = nums[i] - nums[i - 1]

    return minSubArraySum

