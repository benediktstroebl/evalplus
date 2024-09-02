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
    min_sum = nums[0]
    min_len = 1
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            min_sum = max(min_sum + nums[i], min_sum)
        else:
            min_sum = min_sum + nums[i]
        min_len = i
    return min_sum - nums[min_len]