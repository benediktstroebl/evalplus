import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    i = 0
    j = 0
    min_sum = sys.maxsize
    sum = 0
    while i < len(nums):
        sum += nums[i]
        if sum < min_sum:
            min_sum = sum
        while sum >= 0:
            if j < len(nums):
                sum -= nums[j]
                j += 1
            else:
                break
        i += 1
    
