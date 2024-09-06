import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # You can do this in one pass
    # Time complexity O(n)
    # Space complexity O(1)
    # Related to knapsack problem
    
    # initialize variables
    min_sum = math.inf
    i = 0
    j = 0
    sum = 0
    
    # initialize sum
    sum = sum + nums[0]
    # find min_sum and update i and j
    while i < len(nums) and j < len(nums):
        # check if sum of subarray is greater than 0
        if sum >= 0:
            # check if sum is greater than current min_sum
            if sum < min_sum:
                min_sum = sum
                j = j + 1
        # if sum of subarray is smaller than 0
        else:
            # update i
            i = i + 1
            # update sum
            if i < len(nums):
                sum = sum + nums[i]
        # increment j
        j = j + 1
        # check if j is out of bounds
        if j >= len(nums):
            # increment i
            i = i + 1
            # update sum
            if i < len(nums):
                sum = nums[i]
            # reset j
            j = i + 1
    return min_sum
