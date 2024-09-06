import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sum_so_far = math.inf
    for index, number in enumerate(nums):
        sum_so_far = min(sum_so_far + number, number)
        if sum_so_far == number:
            return sum_so_far
    return sum_so_far
