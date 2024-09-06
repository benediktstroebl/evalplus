import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Time: O(n)
    # Space: O(1)
    min_sum = float('inf')
    min_sum_i = 0
    min_sum_j = len(nums)
    sum_ = 0
    for i, num in enumerate(nums):
        sum_ += num
        min_sum = min(min_sum, sum_)
        if sum_ < 0:
            min_sum_i = i + 1
        if sum_ >= 0:
            min_sum_j = i + 1

    if min_sum_j - min_sum_i >= 2:
        return 0
    else:
        return min_sum

