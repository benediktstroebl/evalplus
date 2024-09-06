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

    minSubArraySum = sum(nums)
    minSubArraySum = math.inf

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            print(i, j, sum(nums[i:j + 1]))
            minSubArraySum = min(minSubArraySum, sum(nums[i:j + 1]))

    return minSubArraySum
