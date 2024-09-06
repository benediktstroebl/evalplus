import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # check if the input is not empty
    if not nums:
        return -1
    
    # find the sum of the numbers in the input
    num_sum = sum(nums)
    
    # initialize the min sum to the sum of the input
    min_sum = num_sum
    
    # iterate through the input
    for i in range(len(nums)):
        # initialize the min sum to the sum of the sub-array
        sub_sum = num_sum - nums[i]
        
        # check if the sub-array is not empty
        if i + 1 < len(nums) and nums[i+1] >= 0:
            # update the min sum to be the minimum of the current sub-array sum and the sum of the next sub-array
            sub_sum = min(sub_sum, num_sum - nums[i+1])
        
        # update the min sum if it's smaller than the current minimum
        min_sum = min(min_sum, sub_sum)
        
        # if the current sum is the minimum, update the min sum
        if sub_sum == min_sum:
            min_sum = sub_sum
    
    return min_sum