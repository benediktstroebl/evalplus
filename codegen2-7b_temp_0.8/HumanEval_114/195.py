import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    for i in range(len(nums)):
        current_sum = nums[i]
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum > min_sum:
                min_sum = current_sum
            if current_sum < 0:
                break
    return
