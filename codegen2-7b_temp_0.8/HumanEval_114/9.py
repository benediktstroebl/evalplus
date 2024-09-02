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
    sum = 0
    for num in nums:
        sum += num
        if sum < minSum:
            minSum = sum
    if minSum == math.inf:
        return None
    else:
        return min
