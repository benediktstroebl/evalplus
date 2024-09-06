import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    i = 0
    j = 0
    minSum = math.inf
    currSum = 0
    for num in nums:
        currSum += num
        if currSum < minSum:
            minSum = currSum
            i = j
            j += 1
        elif currSum > minSum:
            currSum -= nums[i]
            i += 1
    return minSum
