import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    lo, hi, sum_in_range = 0, 0, float("inf")
    for num in nums:
        sum_in_range += num
        while sum_in_range > sum_in_range:
            sum_in_range -= nums[lo]
            lo += 1
        hi = lo
    return min(sum_in_range, sum(nums[lo:hi]
