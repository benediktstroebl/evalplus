import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    def _minSubArraySum(arr):
        total = 0
        min_sum = math.inf
        for el in arr:
            total += el
            min_sum = min(min_sum, total)
            total = total - el if total > 0 else total
        return min_sum if min_sum != math.inf else 0

    return _minSubArraySum(nums)
