import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Runtime: 128ms
    # Memory: 15.1MB
    l = len(nums)
    min_length = math.inf
    for cur_len in range(1, l + 1):
        for cur_start in range(l - cur_len + 1):
            cur_nums = nums[cur_start:cur_start + cur_len]
            min_length = min(min_length, sum(cur_nums))
    return min_length
