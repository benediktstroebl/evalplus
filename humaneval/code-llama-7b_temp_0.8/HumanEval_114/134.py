import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Initialize variables
    minSum = math.inf
    currSum = 0

    # Iterate through nums list
    for num in nums:
        currSum += num
        # Update minSum
        if currSum < minSum:
            minSum = currSum

        # If current sum is negative, reset it to zero
        if currSum < 0:
            currSum = 0

    return minSum
