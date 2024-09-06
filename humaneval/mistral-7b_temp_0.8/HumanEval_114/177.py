import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_sum = nums[0]
    left = 0
    right = 0

    while right < len(nums):
        if left < right and nums[left] == 0:
            left += 1

        min_sum = min(min_sum, sum(nums[left:right]))
        right += 1

    return min_sum
