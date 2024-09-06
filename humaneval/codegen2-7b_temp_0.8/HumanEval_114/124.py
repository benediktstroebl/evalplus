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
    i = 0
    j = 0
    while j < len(nums):
        current_sum = nums[j]
        while i <= j and current_sum <= 0:
            current_sum += nums[i]
            i += 1
        min_sum = min(min_sum, current_sum)
        j += 1
    
