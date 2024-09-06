import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums == None or len(nums) == 0:
        return 0

    curr_sum = nums[0]
    min_sum = curr_sum
    for i in xrange(1, len(nums)):
        if curr_sum >= 0:
            curr_sum += nums[i]
        else:
            curr_sum = nums[i]
        if min_sum > curr_sum:
            min_sum = curr_sum

    return min_sum
