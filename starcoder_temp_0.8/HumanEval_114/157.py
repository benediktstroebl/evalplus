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

    # set minimum and current
    minimum = nums[0]
    current = 0

    # loop through nums
    for num in nums:
        current = max(current + num, num)
        minimum = min(minimum, current)

    return minimum
