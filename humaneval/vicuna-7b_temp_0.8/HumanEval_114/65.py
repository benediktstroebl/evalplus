import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    min_sum = float('inf')
    for i in range(n):
        for j in range(i):
            sub_sum = nums[i] + nums[j+1]
            if sub_sum >= 0:
                if sub_sum < min_sum:
                    min_sum = sub_sum
    return min_sum