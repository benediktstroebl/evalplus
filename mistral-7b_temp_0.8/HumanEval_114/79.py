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

    min_sum = nums[0]
    max_sum = nums[0]
    min_start = 0
    for i in range(1, len(nums)):
        if nums[i] > max_sum:
            max_sum = nums[i]
            min_start = i
        elif nums[i] < min_sum:
            min_sum = nums[i]
        elif nums[i] == min_sum or nums[i] == max_sum:
            min_start = i
    return min_sum

