import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    left = right = 0
    for i in range(len(nums)):
        if right < i:
            min_sum = min(min_sum, nums[right] - nums[left])
            left = right = i
        min_sum = min(min_sum, nums[right] - nums[left])
        right += 1

    return min_sum

