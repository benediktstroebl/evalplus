import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    left, right, total = 0, 0, math.inf
    while right < len(nums):
        total += nums[right]
        while left <= right and total >= nums[left]:
            total -= nums[left]
            left += 1
        right += 1
    return total if total <= math.inf else -1
