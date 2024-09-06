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
    min_sum = sum(nums)
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            current_sum = sum(nums[i : j + 1])
            if current_sum < min_sum:
                min_sum = current_sum
    return min_sum

