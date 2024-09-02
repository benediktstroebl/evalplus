import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 1. sliding window
    # 2. two pointers, left, right
    left, right = 0, 0
    left_total, right_total = 0, 0
    min_len = len(nums)
    min_val = math.inf
    while left <= right and right < len(nums):
        right_total += nums[right]
        min_len = min(right - left + 1, min_len)
        min_val = min(min_val, right_total)
        if right_total >= 0:
            right += 1
        else:
            left_total += nums[left]
            left += 1
            right_total = 0
    return min_len, min_val

