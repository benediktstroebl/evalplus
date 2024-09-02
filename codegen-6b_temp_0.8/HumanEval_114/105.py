import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    # use kadane's algorithm
    min_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        tmp = max_sum
        # find max sum subarray
        max_sum = max(nums[i], nums[i] + tmp)
        # find min sum subarray
        min_sum = min(min_sum, max_sum)

    return min_sum

