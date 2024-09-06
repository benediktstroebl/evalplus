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
        return None
    total = nums[0]
    min_sum = nums[0]
    i = 0
    j = 0
    length = len(nums)
    while i < length:
        while j < length and total < 0:
            total += nums[j]
            j += 1
        if total >= 0:
            min_sum = min(min_sum, total)
        total -= nums[i]
        i += 1
    return min_sum
