import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sum = 0
    min = math.inf
    for num in nums:
        sum += num
        if sum < min:
            min = sum
        if sum < 0:
            sum = 0
    if min == math.inf:
        return 0
    else:
        return min
