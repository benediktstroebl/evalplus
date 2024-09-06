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
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    prev_sum = [0] * n
    prev_sum[0] = nums[0]
    prev_sum[1] = min(nums[0], nums[1])

    for i in range(2, n):
        prev_sum[i] = min(prev_sum[i-1] + nums[i], prev_sum[i-2] + nums[i])

    return prev_sum[-1]

