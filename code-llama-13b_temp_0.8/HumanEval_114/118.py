import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    left = 0
    right = 1
    while left < len(nums) and right <= len(nums):
        sub_sum = sum(nums[left:right])
        if sub_sum < min_sum:
            min_sum = sub_sum
        left += 1
        right += 1

    return min_sum

