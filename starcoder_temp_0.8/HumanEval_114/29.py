import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # The two pointer solution.
    min_sum = math.inf
    left = 0
    right = 0
    while right < len(nums):
        min_sum = min(min_sum, sum(nums[left:right+1]))
        right += 1
    return min_sum
