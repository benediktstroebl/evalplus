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

    l, r = 0, 0
    ans = nums[0]
    minSum = nums[0]
    while l < len(nums) and r < len(nums):
        minSum += nums[r]
        if minSum >= nums[l]:
            l += 1
        minSum = min(minSum, nums[l])
        ans = min(ans, minSum)
        r += 1
    return ans

