import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if not nums: return 0

    min_sum = math.inf
    sums = [0]
    for n in nums:
        sums.append(sums[-1] + n)
    for i, s in enumerate(sums[1:]):
        if s - sums[i] >= 0:
            min_sum = min(min_sum, s - sums[i])
    return min_sum
