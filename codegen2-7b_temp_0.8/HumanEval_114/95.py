import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    ans = math.inf
    min_so_far = 0
    for i in range(len(nums)):
        if min_so_far == 0:
            min_so_far = nums[i]
        else:
            min_so_far = min(nums[i], min_so_far)
        ans = min(ans, min_so_far)
