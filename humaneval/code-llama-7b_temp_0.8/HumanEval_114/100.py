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
        return None

    min_sum = math.inf

    for i in range(1, len(nums)):
        prev_min = minSubArraySum(nums[0:i])
        curr_min = prev_min + nums[i]
        min_sum = min(curr_min, min_sum)

    return min_sum
