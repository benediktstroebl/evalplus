import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    numsLen = len(nums)
    result = []
    minimum = float('inf')
    for i in range(numsLen):
        result.append(0)
    for x in range(numsLen):
        result[x] = nums[x]
        for y in range(x+1, numsLen):
            result[x] += nums[y]
            if result[x] <= minimum:
                minimum = result[x]
    return minimum
