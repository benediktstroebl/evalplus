import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # worst case scenario
    # if sum(nums) == 0, all sub-arrays sum to 0
    # so return 0
    if sum(nums) == 0:
        return 0
    
    # set min so large we can later find something smaller
    min_sum = math.inf
    
    # this will be the starting index of the sub-array
    # we will find the min for
    i = 0
    
    # iterate through nums
    for j in range(len(nums)):
        # update the min_sum
        # if it is smaller than current min_sum
        min_sum = min(min_sum, sum(nums[i:j+1]))
        
        # if min_sum is smaller than 0,
        # then we already have found a sub-array
        # that sums to 0
        # and we can return 0
        if min_sum == 0:
            return 0
        
        # if min_sum is the same as sum(nums)
        # we know that we found a sub-array
        # that sums to the sum of nums, which is the
        # overall minimum sub-array sum
        if min_sum == sum(nums):
            return min_sum
        
        # if sum(nums[i:j+1]) is smaller than 0
        # we know that we can skip ahead
        # to where the sum changes sign
        if sum(nums[i:j+1]) < 0:
            # update i to be current j+1
            i = j + 1
            
    return min_sum
