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
    for i in range(0, len(nums)):
        total += nums[i]
        while total >= min_sum:
            min_sum = min(total, min_sum)
            total -= nums[i]
            i += 1
            if i == len(nums):
                break
    return min_sum
