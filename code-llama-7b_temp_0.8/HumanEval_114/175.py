import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # O(n) solution
    sum = 0
    min_sum = math.inf
    for num in nums:
        sum += num
        min_sum = min(sum, min_sum)
        if sum < 0:
            sum = 0
    return min_sum
