import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    l = len(nums)
    min_sum = math.inf
    for i in range(l, 1, -1):
        for j in range(l - i + 1):
            min_sum = min(sum(nums[j:j + i]), min_sum)
    if min_sum == math.inf:
        return 0
    return min_sum
