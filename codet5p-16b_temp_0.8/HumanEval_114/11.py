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
        
    window_sum = 0
    min_sum = math.inf

    for num in nums:
        window_sum += num
        if window_sum < 0:
            window_sum = 0
        if window_sum < min_sum:
            min_sum = window_sum

    return min_sum
