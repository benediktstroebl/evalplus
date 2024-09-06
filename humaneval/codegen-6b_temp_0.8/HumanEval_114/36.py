import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    best_sums = [nums[0]]
    min_sum = nums[0]
    for i in range(1, len(nums)):
        best_sums.append(max(nums[i], best_sums[-1] + nums[i]))
        min_sum = min(best_sums[-1], min_sum)
    return min_sum
