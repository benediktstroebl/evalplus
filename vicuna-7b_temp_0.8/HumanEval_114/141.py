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
    else:
        i, j = 0, 0
        min_sum = nums[0]
        while i < j:
            if nums[i] >= nums[j]:
                i += 1
            else:
                j += 1
        return min_sum
