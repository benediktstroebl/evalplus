import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = math.inf
    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums)):
        if len(nums[i:]) > 1:
            currSum = sum(nums[i:])
            if currSum < minSum:
                minSum = currSum
        else:
            return nums[0]
    return minSum
