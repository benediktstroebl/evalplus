import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    #First, we will find the sum of the list
    total = 0
    for i in nums:
        total += i

    #Then we can use that to find the minimum sub array sum
    minimum = total
    current = 0

    for i in nums:
        current += i
        if current < minimum:
            minimum = current
        if current > 0:
            current = 0

    return minimum
