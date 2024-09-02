import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # check if subarray sum is equal to zero
    if sum(nums) == 0:
        return 0
    
    # initialize maximum value to infinity
    minimum_sum = math.inf
    
    # iterate through the array
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i == j:
                if nums[i] < minimum_sum:
                    minimum_sum = nums[i]
            else:
                if sum(nums[i:j + 1]) < minimum_sum:
                    minimum_sum = sum(nums[i:j + 1])
    
    return minimum_sum
