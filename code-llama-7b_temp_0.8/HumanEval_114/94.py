import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Get the length of the array
    length = len(nums)

    # Create a variable to keep track of the min sum
    min_sum = math.inf

    # Loop through the array
    for i in range(0, length):
        # If the current sum is smaller than the min sum, update min sum
        if sum(nums[i:]) < min_sum:
            min_sum = sum(nums[i:])

    return min_sum
