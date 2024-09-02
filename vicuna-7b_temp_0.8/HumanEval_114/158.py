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
        left = max(nums)
        right = 0
        result = 0
        for i in range(1, len(nums)):
            if nums[i] >= left:
                right = i
                result = max(result, left + nums[i])
            else:
                result = max(result, left - nums[i])
        return result
