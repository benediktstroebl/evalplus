import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    ## Clip
    if len(nums) <= 0:
        return 0

    ## Initialize
    minSum = math.inf
    total = 0

    for n in nums:
        total += n
        minSum = min(minSum, total)

    if total < 0:
        return total
    else:
        return minSum
