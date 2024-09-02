import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    for i in range(len(nums)):
        #get the prefix sum of subarray starting at i
        cur_sum = sum(nums[i:])
        # compare prefix sum to min_sum
        min_sum = min(min_sum, cur_sum)
    return min_sum
