import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) < 1:
        return 0
    
    ans = math.inf
    total = 0
    for i in range(0, len(nums)):
        total += nums[i]
        ans = min(ans, total)
        if total > 0:
            total = 0

    return ans if ans != math.inf else 0
