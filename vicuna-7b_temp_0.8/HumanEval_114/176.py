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
    sums = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            sums[i] = nums[i] + sums[j]
        for j in range(len(nums), i):
            sums[i] = min(nums[i], sums[j-1] + nums[i])
    return sum(sums)
