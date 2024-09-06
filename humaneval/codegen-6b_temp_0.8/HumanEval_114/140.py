import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right, min_sum, min_left, min_right, min_left_sum, min_right_sum = 0, 0, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')
    min_sum = float('inf')

    while right < len(nums):
        min_sum = min(min_sum, nums[right])
        min_right = min(min_right, nums[right])
        min_left_sum = min(min_left_sum, min_left + nums[right])
        min_right_sum = min(min_right_sum, min_right)
        min_left = min(min_left, nums[left])
        min_right = min(min_right, nums[right])
        left += 1
        right += 1
    return min_sum
