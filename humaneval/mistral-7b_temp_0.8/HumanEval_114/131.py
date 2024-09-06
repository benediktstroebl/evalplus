import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = 0
    min_sum = math.inf
    current_sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
        if sum > min_sum:
            current_sum = sum
            sum = 0
        elif sum < min_sum:
            min_sum = sum

    return min_sum
