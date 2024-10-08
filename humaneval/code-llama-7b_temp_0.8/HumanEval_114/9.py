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

    min_sum = 0
    max_sum = nums[0]

    for num in nums[1:]:
        min_sum = min(min_sum, max_sum)
        max_sum += num

    return min(min_sum, max_sum)

