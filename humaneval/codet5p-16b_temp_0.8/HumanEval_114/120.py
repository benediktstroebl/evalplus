import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    
    total = sum(nums)
    if total <= 0:
        return min(nums)
    
    length = len(nums)
    if length <= 1:
        return 0
    
    sums = [0] * length
    sums[0] = nums[0]
    for i in range(1, length):
        sums[i] = sums[i-1] + nums[i]
    
    min_sum = math.inf
    for i in range(0, length):
        for j in range(i+1, length):
            total = sums[j] - sums[i] + nums[i]
            min_sum = min(min_sum, total)
    
    return min_sum
