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
    curr_sum = 0
    min_sum = nums[0]
    for i in range(len(nums)):
        if i == 0:
            curr_sum = nums[i]
        else:
            curr_sum = curr_sum + nums[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
        elif curr_sum >= min_sum:
            pass
    return min_sum
