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

    # 维护一个和最小值，一个和最大值，和最大值跟索引，和最小值跟索引
    minSum = sum(nums)
    maxSum = sum(nums)
    maxIndex = 0
    minIndex = 0
    for i in range(0, len(nums)):
        if maxSum < 0:
            maxSum = 0
            maxIndex = i
        maxSum += nums[i]
        if maxSum < minSum:
            minSum = maxSum
            minIndex = maxIndex
            maxIndex = i + 1
        elif maxSum == minSum:
            if i - maxIndex + 1 < minIndex - minIndex + 1:
                minIndex = maxIndex
    return minSum
