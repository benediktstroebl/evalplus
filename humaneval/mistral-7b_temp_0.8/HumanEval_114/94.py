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
        return None
    if len(nums) == 1:
        return nums[0]
    min_sum = float('inf')
    # We keep track of the sum in the window
    window_sum = 0
    min_len = float('inf')
    for i in range(0, len(nums)):
        window_sum += nums[i]
        while window_sum > 0:
            window_sum -= nums[i - min_len]
            min_sum = min(min_sum, window_sum)
            min_len -= 1

    return min_sum

