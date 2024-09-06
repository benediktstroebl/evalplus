import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 1, 1
    for i in range(1, len(nums)):
        if nums[i] < nums[left]:
            right = i
        elif nums[i] > nums[right]:
            left = i
        else:
            sub = nums[left] to nums[right]
            if sum(sub) == len(sub) // 2:
                return sum(sub)
            left, right = right, left + 1
    return 0
