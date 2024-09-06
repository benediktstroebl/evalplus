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
    sums = [nums[0]] * n
    for i in range(1, n):
        sums[i] = sums[i - 1] + nums[i]
    min_sum = math.inf
    for i in range(n):
        for j in range(i + 1, n + 1):
            sum = sums[j] - sums[i]
            min_sum = min(min_sum, sum)
    return min_sum
