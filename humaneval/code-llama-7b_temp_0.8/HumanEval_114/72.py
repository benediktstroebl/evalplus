import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    if n == 1:
        return nums[0]

    start = 0
    end = 1
    min_sum = nums[0] + nums[1]
    while end < n:
        if nums[end] + nums[start] < min_sum:
            min_sum = nums[end] + nums[start]
        elif nums[end] + nums[start] > min_sum:
            start += 1
            end = start + 1
        else:
            end += 1

    return min_sum



