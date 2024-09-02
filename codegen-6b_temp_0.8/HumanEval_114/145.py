import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # brute force
    min_val = max_val = sum(nums)
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            s = sum(nums[i:j+1])
            if s < min_val:
                min_val = s
            if s > max_val:
                max_val = s
    return min_val, max_val

