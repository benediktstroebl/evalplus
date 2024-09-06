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
    min_idx = 0
    
    for i in range(1, len(nums)):
        sum_ = nums[i]
        cur_sum = sum_ + nums[i-1]
        if cur_sum < min_sum:
            min_sum = cur_sum
            min_idx = i

    return min_sum,
