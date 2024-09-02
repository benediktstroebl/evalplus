import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = 0
    sub_array_sum = math.inf
    for i in range(0, len(nums)):
        total += nums[i]
        for j in range(i, len(nums)):
            sub_array_sum = min(sub_array_sum, total)
            total -= nums[j]
    return sub_array_sum

