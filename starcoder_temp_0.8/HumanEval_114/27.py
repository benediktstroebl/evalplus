import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    result = 0
    current_sum = 0
    lowest_sum = math.inf
    for num in nums:
        current_sum += num
        if current_sum < lowest_sum:
            lowest_sum = current_sum
        if current_sum > 0:
            result = current_sum
        else:
            current_sum = 0
    return result
