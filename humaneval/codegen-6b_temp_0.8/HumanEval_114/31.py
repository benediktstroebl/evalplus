import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Try to find a subarray that sums to 0
    if sum(nums) == 0:
        return 0
    # Find the min sum non-zero subarraay
    minSum = 1 << 32;
    minSumArr = [0]
    for i in range(len(nums)):
        minSum = min(minSum, nums[i])
        minSumArr.append(minSum)
    minSumArr.pop()
    minSumArr.append(0)
    for i in range(len(nums)):
        minSumArr[i] += minSumArr[i - 1]
    minSum = 1 << 32
    for i in range(len(minSumArr)):
        minSum = min(minSum, minSumArr[i])
    return minSum

