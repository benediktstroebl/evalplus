import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize the minimum sum to math.inf
    min_sum = math.inf

    # Iterate through the array
    for i in range(len(nums)):
        # Initialize the current sum to the sum of the array so far
        current_sum = nums[i]
        # If the array has not been fully processed, add the current element
        # to the current sum
        if i < len(nums) - 1:
            current_sum += nums[i+1]
        # Update the minimum sum
        min_sum = min(min_sum, current_sum)

    return min_sum
