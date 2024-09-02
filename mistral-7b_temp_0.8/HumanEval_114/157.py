import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min = math.inf
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            temp = sum(nums[i:j + 1])
            if temp < min:
                min = temp
    return min
