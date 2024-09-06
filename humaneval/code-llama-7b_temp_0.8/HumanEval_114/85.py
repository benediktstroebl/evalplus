import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize a running minimum variable and a sum variable
    runningMin, sum = math.inf, 0
    # Traverse the array
    for i in nums:
        # Update the sum and running minimum
        sum += i
        runningMin = min(runningMin, sum)
    return runningMin











