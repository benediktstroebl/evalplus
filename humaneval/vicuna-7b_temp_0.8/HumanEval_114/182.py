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
    for i in range(1, n):
        for j in range(0, i):
            for k in range(i+1, n):
                for l in range(j+1, k):
                    s = sum(nums[j:k])
                    if s < sum(nums[j+1:k+1]):
                        return s
    return sum(nums)
