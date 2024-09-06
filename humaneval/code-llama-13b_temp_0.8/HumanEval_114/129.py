import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Check for empty list:
    if nums == []:
        return "The given array is empty."
    
    # Initialize variables:
    length = len(nums)
    minimum = math.inf

    # Find minimum:
    for i in range(0, length):
        for j in range(i, length):
            # If it is greater than 0, then add it to the sum:
            if minimum > 0:
                minimum += nums[j]
            # Otherwise, reset the value to the sum of the current subarray:
            else:
                minimum = nums[j]
            # If the sum is less than the current minimum, then change the minimum:
            if minimum < min:
                minimum = sum(nums[i:j+1])
        # Reset minimum variable:
        minimum = math.inf
    
    # Return the minimum sum:
    return minimum

