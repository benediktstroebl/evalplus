import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    l = len(nums)
    if l == 0:
        return 0
    left = 0
    sum = 0
    minimum = math.inf
    for right in range(l):
        sum += nums[right]
        if sum < minimum:
            minimum = sum
        while sum >= minimum:
            left = right+1
            sum -= nums[left-1]
    return minimum
