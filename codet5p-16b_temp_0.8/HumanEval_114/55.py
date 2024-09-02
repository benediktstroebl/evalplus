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
    min_sum = math.inf
    for i, num in enumerate(nums):
        total += num
        if total < min_sum:
            min_sum = total
        while total >= min_sum:
            total -= nums[i]
            i += 1
    return min_sum

