import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    min_sum = float('inf')

    for i in range(1, len(nums)):
        cur_sum = nums[i-1] + nums[i]
        if cur_sum < min_sum:
            min_sum = cur_sum

    return min_sum







