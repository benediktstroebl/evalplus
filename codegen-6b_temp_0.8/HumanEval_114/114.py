import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    g = [0]*len(nums)
    g[0] = nums[0]
    for i in range(1,len(nums)):
        g[i] = g[i-1] + nums[i]
    print(g)
    min = math.inf
    for i in range(len(nums)):
        for j in range(0,i+1):
            curr = g[i] - g[j]
            if curr < min:
                min = curr
    return min

