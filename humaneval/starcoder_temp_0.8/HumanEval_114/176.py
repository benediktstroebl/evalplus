import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    current_sum = nums[0]
    min_sum = current_sum
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        min_sum = min(current_sum, min_sum)
    return min_sum
