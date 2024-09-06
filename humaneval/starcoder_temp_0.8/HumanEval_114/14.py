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
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    cur_sum = min_sum = nums[0]
    for i in range(1, len(nums)):
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += nums[i]
        min_sum = min(min_sum, cur_sum)
    return min_sum
