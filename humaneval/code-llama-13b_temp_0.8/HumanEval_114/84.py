import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Assume that nums is a list
    # Loop through nums and calculate the sum
    # Then, compare the sum with the min_sum
    # Update min_sum if sum < min_sum
    min_sum = math.inf
    sum = 0

    for i in range(len(nums)):
        sum += nums[i]
        if sum < min_sum:
            min_sum = sum
        if sum < 0:
            sum = 0
    return min_sum

