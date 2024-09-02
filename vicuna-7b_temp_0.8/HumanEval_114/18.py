import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Check if the array is empty
    if not nums:
        return -1
    
    # Initialize variables
    max_sum = 0
    curr_sum = 0
    curr_len = 0
    
    # Iterate through the array
    for num in nums:
        # Update the sum
        curr_sum += num
        
        # Check for a new max sum and update it if necessary
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_len = curr_len
            
        # Update the length of the current sub-array
        curr_len += 1
        
        # If the current sum is greater than the max sum, reset the max sum and len
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_len = curr_len
            
    # Return the minimum sum of a non-empty sub-array
    return max_sum
