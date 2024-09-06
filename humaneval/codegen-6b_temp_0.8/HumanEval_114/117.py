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

    min_total = nums[0]
    min_num = nums[0]

    for num in nums[1:]:
        min_total = min(min_total + num, num)
        min_num = min(min_num, min_total)
    return min_num
