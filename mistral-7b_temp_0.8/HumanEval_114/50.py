import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    length = len(nums)
    if length == 0:
        return 0
    total = nums[0]
    min_subarray = nums[0]
    for i in range(1, length):
        total += nums[i]
        if total < min_subarray:
            min_subarray = total
        elif total > 0:
            continue
        else:
            total = 0
    return min_subarray
