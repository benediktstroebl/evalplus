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
    
    nums.sort()
    left = 0
    right = 1
    while left < right:
        middle = (left + right) // 2
        if nums[middle] == nums[left]:
            left = middle + 1
        else:
            right = middle
    return left
