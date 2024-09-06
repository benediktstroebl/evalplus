import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # handle the edge case of an empty array
    if not nums:
        return 0
    
    # sort the array
    nums.sort()
    
    # initialize the sum and start of the current sub-array
    current_sum = nums[0]
    current_start = 0
    
    # iterate over the remaining elements in the array
    for i in range(1, len(nums)):
        # update the current sum and start of the sub-array
        current_sum += nums[i]
        current_start = i + current_sum
        
        # check if the current sub-array is non-empty
        if current_start < len(nums):
            # update the minimum sum of any non-empty sub-array
            if current_sum < minSum:
                minSum = current_sum
            
    return minSum
