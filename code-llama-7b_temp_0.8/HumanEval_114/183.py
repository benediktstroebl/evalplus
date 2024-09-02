import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    #stores the min and max value for the subarray
    min_sum = math.inf
    max_sum = -math.inf
    #stores the sum of the subarray
    running_sum = 0
    for i in nums:
        running_sum += i
        if running_sum < min_sum:
            min_sum = running_sum
        if running_sum > max_sum:
            max_sum = running_sum
    if min_sum == math.inf:
        return 0
    return min_sum
