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
    elif len(nums) == 1:
        return nums[0]
    else:
        sum = 0
        mini = math.inf
        for i in range(len(nums)):
            sum += nums[i]
            if sum > mini:
                mini = sum
        return mini
