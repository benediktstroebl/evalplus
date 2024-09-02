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
    min_length = 1
    best_sum = math.inf
    left, right = 0, 0
    while left < len(nums) - min_length + 1:
        current_sum = sum(nums[left : left + min_length])
        if current_sum < best_sum:
            best_sum = current_sum
        if current_sum >= min_sum:
            min_sum = current_sum
            min_length += 1
            right = left + min_length - 1
        left += 1
    return best_sum

