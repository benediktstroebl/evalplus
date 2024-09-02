import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_value = math.inf
    current_value = 0

    for num in nums:
        current_value = current_value + num
        if current_value < min_value:
            min_value = current_value

        if current_value < 0:
            current_value = 0

    return min_value
