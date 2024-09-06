import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # sum(nums[:i]) -> subarray
    # sum(nums[j:]) -> subarray
    # sum(nums) = sum(nums[:i]) + sum(nums[j:])
    # sum(nums[:i]) - sum(nums[j:]) = sum(nums[j:])

    n = len(nums)
    sums = [0] * (n + 1)
    for i in range(1, n + 1):
        sums[i] = sums[i - 1] + nums[i - 1]

    min_sum = math.inf
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            sub = sums[j] - sums[i - 1]
            if sub < min_sum:
                min_sum = sub
    return min_sum
