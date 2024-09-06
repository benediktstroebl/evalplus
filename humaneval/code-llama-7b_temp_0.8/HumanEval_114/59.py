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
    if len(nums) == 1:
        return nums[0]

    minSum = math.inf
    prefix = [None] * (len(nums) + 1)

    for i, n in enumerate(nums):
        prefix[i + 1] = prefix[i] + n if prefix[i] else n
        if prefix[i] < minSum:
            minSum = prefix[i]

    for i in range(1, len(prefix)):
        if prefix[i] - minSum >= 0:
            return minSum

    return minSum
