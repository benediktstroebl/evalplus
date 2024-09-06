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
    if n == 0:
        return 0
    min_sum = math.inf
    if n == 1:
        return nums[0]

    for i in range(n):
        for j in range(i+1,n+1):
            s = sum(nums[i:j])
            if s < min_sum:
                min_sum = s
    return min_sum
