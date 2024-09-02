import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 1, nums[0]
    for i in range(1, len(nums)):
        if nums[i] < nums[left]:
            left = i
        elif nums[i] > nums[right]:
            right = i
        else:
            if right - left + 1 != nums[i]:
                continue
            left, right = right, i
    if left < right:
        return (left + 1, nums[left])
    else:
        return (right, 0)
