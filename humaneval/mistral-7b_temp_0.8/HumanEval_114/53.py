import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    current_sum = 0
    min_sum = math.inf
    for num in nums:
        if current_sum + num >= 0:
            current_sum += num
            min_sum = min(min_sum, current_sum)
        else:
            current_sum = num
    return min_sum
