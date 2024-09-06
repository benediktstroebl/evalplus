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

    min_sum = math.inf
    min_diff = math.inf
    cur_sum = 0

    for i, num in enumerate(nums):
        cur_sum += num
        min_diff = min(min_diff, cur_sum - min_sum)
        min_sum = min(min_sum, cur_sum)

    return min_diff
