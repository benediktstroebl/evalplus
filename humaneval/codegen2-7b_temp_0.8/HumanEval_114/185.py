import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    curr_sum = nums[0]
    curr_min = nums[0]
    curr_min_index = 0
    for i in range(1,len(nums)):
        curr_sum += nums[i]
        if curr_sum < curr_min:
            curr_min = curr_sum
        else:
            curr_sum = nums[i
