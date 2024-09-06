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
    currentSum = nums[0]
    globalSum = nums[0]
    for num in nums[1:]:
        currentSum = max(num, currentSum + num)
        globalSum = min(globalSum, currentSum)
    return globalSum
