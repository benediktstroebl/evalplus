import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = sum(nums)
    # using two pointers, compare subarray sums
    left, right = 0, 0
    while right < len(nums):
        minSum = min(minSum, sum(nums[left : right + 1]))
        # find next right
        if sum(nums[left : right + 1]) >= 0:
            right += 1
        else:
            left += 1
            right = left
    return minSum
