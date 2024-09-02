import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # keep track of the minimum sum and the start index
    min_sum = nums[0]
    start_index = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            min_sum = min(min_sum, nums[i])
        else:
            min_sum += nums[i]
    return min_sum
