import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = float('inf')
    minSumIndex = None
    def computeSum(start, end):
        return sum(nums[start:end])
    for i in range(len(nums)):
        # If we haven't seen a sumof < 0, start a new subarray
        if minSumIndex is None and computeSum(i, len(nums)) < 0:
            minSumIndex = i
        # Else, if we're within the active subarray, extend it
        elif computeSum(i, len(nums)) < 0:
            minSumIndex = min(minSumIndex, i)
        # Check if we're at the last index
        elif i == len(nums)-1:
            minSum = min(minSum, computeSum(i, len(nums)))

    return minSum if minSumIndex is None else -1
