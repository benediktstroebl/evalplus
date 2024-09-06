import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sums = [0 for i in range(len(nums) + 1)]
    sums[0] = 0
    result = float('inf')
    for i in range(1, len(nums) + 1):
        sums[i] = sums[i - 1] + nums[i - 1]

    for i in range(1, len(nums) + 1):
        for j in range(i, len(nums) + 1):
            subarray = sums[j] - sums[i - 1]
            if subarray < result:
                result = subarray

    return result
