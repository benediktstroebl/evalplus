import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 1:
        return nums[0]

    totalSum = sum(nums)
    leftPointer = 0
    minSum = math.inf

    for rightPointer in range(len(nums)):
        currentSum = 0
        currentSum += nums[rightPointer]

        while currentSum >= totalSum / 2:
            minSum = min(currentSum, minSum)
            leftPointer += 1
            currentSum -= nums[leftPointer]
    return minSum

