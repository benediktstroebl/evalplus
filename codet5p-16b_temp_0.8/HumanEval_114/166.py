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
    sums = []
    sums.append(nums[0])
    for i in range(1, n):
        sums.append(sums[-1] + nums[i])
    sums = sorted(sums)
    for i in range(1, n):
        if sums[i] - sums[i-1] < nums[i]:
            return sums[i-1]
    return sum(nums)
