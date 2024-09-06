import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    
    result = math.inf
    start = 0
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        while total >= nums[start]:
            result = min(result, total - nums[start])
            total -= nums[start]
            start += 1
    return result if result < math.inf else 0
    
