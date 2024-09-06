import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 0:
        return math.inf

    sum = 0
    min = 0
    for i in range(0, len(nums)):
        sum += nums[i]
        min = min + nums[i] if min < 0 else min
        min = sum if sum < min else min

    return min
