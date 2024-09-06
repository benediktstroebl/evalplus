import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Reminder: we are working with arrays
    # so nums[i] is not an integer, it is an array

    # Loop through the array
    # At the end of each iteration, the minSubArraySum will be:
        # the current value if that value is less than the minSubArraySum
        # the minSubArraySum if that value is greater than the current value

    # The values that will be passed between iterations are:
        # minSubArraySum - the smallest sum seen so far
        # currentValue - the sum of the current array
        # i - the current index
    # The time complexity is O(n)

    minSubArraySum = math.inf
    currentValue = 0
    for i in range(len(nums)):
        currentValue += nums[i]
        if currentValue < minSubArraySum:
            minSubArraySum = currentValue
        elif currentValue > minSubArraySum:
            minSubArraySum += currentValue
    return minSubArraySum
