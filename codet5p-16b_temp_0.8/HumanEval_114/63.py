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
        return None
    if len(nums) == 1:
        return nums[0]
    else:
        minSum = math.inf
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            for j in range(i+1, len(nums)):
                minSum = min(minSum, temp)
                temp -= nums[j-1]
                temp += nums[j]
        return minSum
