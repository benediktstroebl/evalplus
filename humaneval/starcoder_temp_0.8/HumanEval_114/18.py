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
    total, minimum, l, r = nums[0], nums[0], 0, 1
    while r < len(nums):
        total += nums[r]
        while total >= minimum:
            minimum = total
            total -= nums[l]
            l += 1
        r += 1
    return minimum
