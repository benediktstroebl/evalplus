import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    smallest = math.inf
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum < smallest:
            smallest = current_sum
        if current_sum < 0:
            current_sum = 0
    return smallest
