import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Sort the array in descending order
    nums = sorted(nums, reverse=True)
    
    # Initialize the sum and the current index of the current sub-array
    sum = nums[0]
    current_index = 0
    
    # Start iterating from the second element of the array
    for i in range(1, len(nums)):
        # Check if the current sub-array is non-empty
        if sum - nums[i] >= 0:
            # Update the sum and the current index of the current sub-array
            sum -= nums[i]
            current_index += 1
        else:
            # Update the current sub-array
            sum += nums[i]
            current_index = i
    
    return sum
