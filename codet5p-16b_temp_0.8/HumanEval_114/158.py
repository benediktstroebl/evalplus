import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sums = []
    sum = 0
    for i in nums:
        sum += i
        sums.append(sum)

    min_subarray = math.inf
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = sums[j+1] - sums[i]
            if subarray < min_subarray:
                min_subarray = subarray

    return min_subarray
