import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    minimum_sum = math.inf
    total = 0
    for x in nums:
        total += x
        if total < minimum_sum:
            minimum_sum = total
        if total >= minimum_sum:
            total = total - minimum_sum
    return minimum_sum

