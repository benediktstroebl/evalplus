import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    sum, start = nums[0], 0
    for i in range(n):
        sum += nums[i]
        while sum < 0:
            sum += nums[start]
            start += 1
        if sum >= 0:
            break
    sum = math.inf
    return sum if start == 0 else sum - nums
