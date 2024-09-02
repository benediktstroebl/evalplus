import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    subArraySums = [0]
    for i in range(len(nums)):
        subArraySums.append(subArraySums[-1] + nums[i])
    minSum = float('inf')
    for i in range(len(subArraySums)):
        for j in range(i, len(subArraySums)):
            if subArraySums[j] - subArraySums[i] < minSum:
                minSum = subArraySums[j] - subArraySums[i]
    return minSum
