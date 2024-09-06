import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    
    start = 0
    end = 0
    min_so_far = 0
    total = 0
    for i in range(len(nums)):
        total += nums[i]

        while (min_so_far <= total):
            min_so_far = min(min_so_far, total)
            end = i
            total -= nums[start]
            start += 1
        
    return min_so_far
