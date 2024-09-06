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
    
    if len(nums) == 1:
        return nums[0]
    
    min_sum = math.inf
    sums = 0
    for num in nums:
        sums += num
        min_sum = min(min_sum, sums)
        if sums < 0:
            sums = 0
    return min_sum
