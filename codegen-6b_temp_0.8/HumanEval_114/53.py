import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    totalSum = 0
    minSum = math.inf
    #start, end, currentSum
    for i, v in enumerate(nums):
        totalSum += v
        #end = i #not last index
        #currentSum = nums[start:end+1] #here we get index range
        if i < len(nums) - 1:
            if totalSum - nums[i+1] < minSum:
                minSum = totalSum - nums[i+1]

    return minSum

