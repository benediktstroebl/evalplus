import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    s = sum(nums)
    if s < 0:
        return math.inf
    
    sums = []
    for n in nums:
        sums.append(sums[-1] + n)
    
    for i in range(len(sums)):
        if sums[i] >= s:
            return s
    
    return
