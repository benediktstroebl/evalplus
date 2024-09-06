import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = 0
    min_so_far = math.inf

    i = 0
    for j in range(len(nums)):
        min_sum += nums[j]
        while i <= j and min_sum < min_so_far:
            min_so_far = min_sum
            min_sum = min_sum - nums[i]
            i += 1
    return min_so_far

