import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Initializations
    minSum = math.inf
    currentSum = 0

    # Loop through the list
    # For each element, add the element to the currentSum
    # If currentSum is smaller than minSum, set minSum to currentSum
    # If currentSum is greater or equal to zero, add it to the minSum
    # If currentSum is negative, reset it to zero
    for num in nums:
        currentSum += num
        if currentSum < minSum:
            minSum = currentSum
        if currentSum >= 0:
            minSum += currentSum
        if currentSum < 0:
            currentSum = 0

    return minSum
