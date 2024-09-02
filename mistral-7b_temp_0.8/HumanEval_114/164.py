import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if not nums:
        return 0

    left, right, min_sum = 0, 0, math.inf
    min_length = math.inf

    for right in range(len(nums)):
        min_sum = min_sum + nums[right]
        while left <= right and min_sum > 0:
            min_sum = min_sum - nums[left]
            left += 1
            min_length = min(min_length, right - left + 1)

    return -1 if min_length == math.inf else min_length

