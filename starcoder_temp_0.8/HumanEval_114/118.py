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
    if len(nums) == 1:
        return nums[0]
    if min(nums) < 0:
        return min(nums)
    sum = [0 for i in range(len(nums))]
    sum[0] = nums[0]
    for i in range(1, len(nums)):
        sum[i] = max(sum[i-1]+nums[i], nums[i])
    return min(sum)
