import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 先求和
    total = sum(nums)
    # 然后以此为最小子数组的起点
    for i in range(len(nums)):
        subtotal = 0
        for j in range(i, len(nums)):
            subtotal += nums[j]
            if subtotal == total:
                return total
            if subtotal < total:
                total = subtotal
    return total

