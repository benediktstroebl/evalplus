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
    if not nums or n == 0:
        return 0

    sum = 0
    l = 0
    r = 0
    min_sum = math.inf

    while r < n:
        sum += nums[r]
        while sum > 0:
            min_sum = min(min_sum, sum)
            sum -= nums[l]
            l += 1
        r += 1

    return min_sum
