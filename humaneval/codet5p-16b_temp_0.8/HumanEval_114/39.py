import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if not nums:
        return math.inf
    n = len(nums)
    min_sum = math.inf
    sum = 0
    left = 0
    for i in range(n):
        sum += nums[i]
        while sum >= min_sum:
            min_sum = sum
            right = i
            left = left + 1
            sum = sum - nums[left]

    return min_sum
