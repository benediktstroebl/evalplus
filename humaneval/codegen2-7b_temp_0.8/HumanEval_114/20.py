import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    num_of_nums = len(nums)
    min_sum = math.inf
    start = 0
    for end in range(1, num_of_nums):
        sum = 0
        for i in range(start, end):
            sum += nums[i]
            min_sum = min(sum, min_sum)
        start = end
    return min_
