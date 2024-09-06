import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    
    result = float("inf")
    curr_sum = 0
    start = 0
    
    for i, val in enumerate(nums):
        curr_sum += val
        
        while curr_sum >= 0:
            result = min(result, curr_sum)
            curr_sum -= nums[start]
            start += 1
        
    return result if result != float("inf") else -1
