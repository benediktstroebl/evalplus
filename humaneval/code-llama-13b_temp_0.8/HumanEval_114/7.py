import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    max_sum = -math.inf
    cur_sum = 0
    # Counting way
    for num in nums:
        cur_sum += num
        if num < 0:
            min_sum = min(min_sum, num)
        max_sum = max(max_sum, num)
        if cur_sum < 0:
            min_sum = min(min_sum, cur_sum)
    return max(min_sum, max_sum, cur_sum)

