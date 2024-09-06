import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Find the min sub array sum of the given array
    minSum = nums[0]
    # Define the start and end pointers
    start = 0
    end = 0
    # Loop through the array
    while(end < len(nums)):
        # Check if the current sum is less than the minimum sum
        if(nums[end] < minSum):
            minSum = nums[end]
        # Update the end pointer
        end += 1

    return minSum
