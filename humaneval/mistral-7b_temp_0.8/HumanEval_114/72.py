import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Runtime: 32 ms, faster than 70.86% of Python3 online submissions for Minimum Subarray.
    # Memory Usage: 14 MB, less than 99.79% of Python3 online submissions for Minimum Subarray.
    if not nums:
        return 0
    n = len(nums)
    min_val = nums[0]
    min_val_index = 0
    current_val = 0
    for i in range(1, n):
        if current_val + nums[i] > min_val:
            min_val = current_val + nums[i]
            min_val_index = i
        current_val += nums[i]
    return nums[min_val_index - n + 2:min_val_index + 1]

