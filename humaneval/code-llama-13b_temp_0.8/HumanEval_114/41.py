import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initial min value
    min_value = math.inf
    # Initial sum
    sum = 0
    # Loop through nums
    for i in nums:
        # Add to sum
        sum += i
        # Check if less than min_value
        if min_value > sum:
            # Reset min value to sum
            min_value = sum
        # If sum is less than 0, add next num to sum
        if sum < 0:
            sum = 0

    # Return min_value
    return min_value
