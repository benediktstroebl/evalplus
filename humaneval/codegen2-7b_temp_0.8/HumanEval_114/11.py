import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min = math.inf
    start = 0
    for i, num in enumerate(nums):
        if num >= 0:
            min = min if min < num else num
            start = i
    sum = 0
    for i in range(start, len(nums)):
        sum += nums[i]
        if sum >= min:
            return min
        
    return
