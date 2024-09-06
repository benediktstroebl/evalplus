import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 0:
        return 0

    # Keep track of the min sum
    minSum = math.inf
    # Keep track of the current sum
    currSum = 0
    # Start at the first number
    index = 0

    # Keep iterating until we reach the end of the list
    while index < len(nums):
        # Add the current number to the current sum
        currSum += nums[index]
        # Keep iterating through the list while the current sum is
        # not greater than the min sum
        while currSum < minSum:
            # Update the minimum sum
            minSum = currSum
            # Increase the index
            index += 1
            # Check if the index is too large
            if index == len(nums):
                break
            # Add the next number in the list to the current sum
            currSum += nums[index]
        # Move on to the next number
        index += 1
    # Return the min sum
    return minSum
