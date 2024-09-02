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
    sum = 0
    min_sum = math.inf
    for num in nums:
        sum += num
        while sum > 0 and min_sum > sum:
            min_sum = sum
            sum -= nums[0]
    return min_sum
