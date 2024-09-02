import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums == []:
        return 0
    minSum = nums[0]

    for i in range(len(nums)):
        if i == 0:
            minSum = nums[i]
        else:
            minSum = min(nums[i],  minSum + nums[i])

    return minSum
