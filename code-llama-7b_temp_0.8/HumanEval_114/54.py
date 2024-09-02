import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    #return min(sum(nums[i:i+j]) for i in range(len(nums)) for j in range(1, len(nums)+1))
    min_sum = float('inf')

    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        min_sum = min(min_sum, sum)

    sum = 0
    for i in range(len(nums)-1, -1, -1):
        sum += nums[i]
        min_sum = min(min_sum, sum)

    return min_sum



