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
    min_start = 0
    min_end = 0
    min_val = math.inf
    for i in range(len(nums)):
        if min_val > min_sum:
            min_val = min_sum
        min_sum = min_sum - nums[min_start] + nums[i]
        min_start = i
    print(min_val)
    return min_val

