import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    summ, count = nums[0], 1
    for idx in range(1, len(nums)):
        if nums[idx] >= nums[idx - 1]:
            count += 1
        else:
            count -= 1
        summ = min(summ, nums[idx - 1])
    if count == 1:
        return summ
    else:
        return -1
