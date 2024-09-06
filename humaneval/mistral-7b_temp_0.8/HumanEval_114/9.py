import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums is None or len(nums) == 0:
        return None
    start = 0
    min_start = 0
    min_sum = math.inf
    for i in range(len(nums)):
        if nums[i] < min_sum:
            start = i
            min_sum = nums[i]
        if i > start:
            if nums[start:i] != 0:
                if min_sum + nums[i] < min_sum:
                    min_start = start
                    min_sum = min_sum + nums[i]
    if min_sum == math.inf:
        return None
    return min_sum
