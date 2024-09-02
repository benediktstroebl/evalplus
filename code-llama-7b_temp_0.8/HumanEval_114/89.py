import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    """
    Iterate through the list and for each item keep track of the cumulative sum.
    """
    cumulative_sum = 0
    min_sum = math.inf
    for num in nums:
        cumulative_sum += num
        min_sum = min(min_sum, cumulative_sum)
        if cumulative_sum < 0:
            cumulative_sum = 0
    return min_sum

















