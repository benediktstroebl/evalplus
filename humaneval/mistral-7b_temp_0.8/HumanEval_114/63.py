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
    nums_sum = 0
    min_sum = nums[0]
    for i in range(len(nums)):
        nums_sum += nums[i]
        if nums_sum > min_sum:
            nums_sum = nums[i]
            min_sum = nums[i]
        elif nums_sum == min_sum:
            nums_sum = nums[i]

        if nums_sum < min_sum:
            min_sum = nums_sum
    return min_sum
