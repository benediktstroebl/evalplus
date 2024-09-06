import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # maxSum = sum(nums)
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         maxSum = min(maxSum, sum(nums[i:j+1]))
    # return maxSum
    minSum = math.inf
    minArr = nums.copy()
    minSum = sum(minArr)

    for i in range(len(nums)):
        minArr[i] = minArr[i] - minArr[i - 1]

    for i in range(len(nums)):
        minSum = min(minSum, sum(minArr[i:]))

    return minSum

