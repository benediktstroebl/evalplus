import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    m, n = len(nums), len(nums[0])
    max_sum = m * n
    for i in range(1, n):
        for j in range(i):
            for k in range(i+1, m):
                sum = nums[j] + nums[k]
                if sum > max_sum:
                    max_sum = sum
    return max_sum
