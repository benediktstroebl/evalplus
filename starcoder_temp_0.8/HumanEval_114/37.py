import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    if n < 1:
        return 0
    else:
        acc = nums[0]
        min_acc = acc
        for i in range(1, n):
            acc = nums[i] + min(acc, 0)
            min_acc = min(min_acc, acc)
        return min_acc
