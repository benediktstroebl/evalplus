import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # sort the array
    nums = sorted(nums)
    
    # initialize the sum of the sub-array to be 0
    current_sum = 0
    
    # iterate through the array
    for i in range(len(nums)):
        # check if the current sub-array sum is 0 or negative
        if current_sum == 0 or current_sum < 0:
            # update the sum of the sub-array
            current_sum = nums[i]
        else:
            # if the current sub-array sum is positive, the current sub-array is the minimum
            return current_sum

    # return -1 if the array is empty
    return -1