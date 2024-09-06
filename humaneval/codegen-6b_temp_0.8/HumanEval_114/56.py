import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # minimize sum of elements in nums from start to end
    # minSum = [float('inf')] * (len(nums) + 1)
    # minSum[0] = 0
    # for i in range(1, len(nums) + 1):
    #     minSum[i] = min(minSum[i - 1] + nums[i - 1], nums[i - 1])
    # return minSum[-1]
    n = len(nums)
    minSum = [float('inf')] * (n + 1)
    minSum[0] = 0
    for i in range(1, n + 1):
        minSum[i] = min(nums[i - 1], minSum[i - 1] + nums[i - 1])
    return minSum[n]
