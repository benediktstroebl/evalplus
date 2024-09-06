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
        return None
    min_sum = nums[0]
    min_len = 1
    for i in range(1, len(nums)):
        sum = nums[i]
        if sum < min_sum:
            min_sum = sum
            min_len = 1
        else:
            min_sum += sum
            if min_sum < min_len:
                min_len = min_sum
    return min_len
