import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    #result = nums[0]
    #subSum = 0
    #for i in xrange(len(nums)):
    #    subSum += nums[i]
    #    if result > subSum:
    #        result = subSum
    #    if subSum < 0:
    #        subSum = 0

    #return result
    # idea is to use sliding window, as seen below
    # could also use hashmaps
    i = 0
    result = nums[0]
    sum = 0
    while i < len(nums):
        if sum + nums[i] < nums[i]:
            sum = 0
            i += 1
        else:
            sum += nums[i]
            result = min(result, sum)
            i += 1
    
    return result
            

