import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sum = math.inf
    left = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub = sum(nums[i:j+1])
            if sub < sum:
                left = i
                sum = sub
    return sum
