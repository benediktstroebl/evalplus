import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    min_sub_array = math.inf
    
    start = 0
    cur_sum = 0
    
    for end in range(len(nums)):
        cur_sum += nums[end]
        
        if cur_sum < min_sub_array:
            min_sub_array = cur_sum
        
        while cur_sum >= 0:
            cur_sum -= nums[start]
            start += 1
