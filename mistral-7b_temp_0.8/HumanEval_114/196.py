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
    start = 0
    end = 0
    for i in range(len(nums)):
        start = end
        end = i
        curr_sum = sum(nums[start:end])
        if curr_sum < min_sum:
            min_sum = curr_sum
    return min_sum
