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
    ans = math.inf
    sum = 0
    while i < len(nums):
        while i < len(nums) and sum < 0:
            sum += nums[i]
            i += 1
        if sum < ans:
            ans = sum
        sum -= nums[i]
        i += 1
    if ans == math.inf:
        return 0
    return ans

