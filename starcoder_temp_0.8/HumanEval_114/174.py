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
    min_length = 1
    for i in range(len(nums)):
        j = i + 1
        while j < len(nums):
            sum_temp = sum(nums[i:j])
            if sum_temp < min_sum:
                min_sum = sum_temp
                min_length = j - i + 1
            j += 1
    return min_sum
