import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def recurse(nums, nums_sum, num_idx, min_sum):
        if nums_sum < min_sum:
            min_sum = nums_sum
        if num_idx == len(nums):
            return min_sum
        return recurse(nums, nums_sum + nums[num_idx], num_idx+1, min_sum)
    
    return recurse(nums, 0, 0, math.inf)
