import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_len = len(nums)
    min_sum = max_len * 2
    for i in range(1, max_len):
        for j in range(i):
            for k in range(j+1, max_len):
                sum = nums[j] + nums[k]
                if sum < min_sum:
                    min_sum = sum
    return min_sum