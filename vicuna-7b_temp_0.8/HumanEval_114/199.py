import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    result = float('inf')
    for i in range(len(nums)-1):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] < 0:
                break
            elif nums[i] + nums[j] <= result:
                result = min(result, nums[i] + nums[j])
            j += 1
    return result
