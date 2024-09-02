import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    low = math.inf
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        low = min(low, sum)
        if sum < 0:
            sum = 0
    if math.inf == low:
        return low
    else:
        return low +
