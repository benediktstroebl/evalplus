import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    
    # create a subSum array
    subSum = [0]
    for i in range(1, len(nums) + 1):
        subSum.append(subSum[-1] + nums[i-1])
    
    # find the min sum
    minSum = math.inf
    for i in range(len(nums)):
        minSum = min(minSum, subSum[i+1])
        
    return minSum
