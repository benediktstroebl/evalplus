import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if nums == []:
        return -math.inf
    if sum(nums) < 0:
        return 0
    n = len(nums)
    curr_sum = sum(nums)
    min_sum = curr_sum
    for i in range(n):
        curr_sum -= nums[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum <= 0:
            curr_sum = 0
    return min_sum
