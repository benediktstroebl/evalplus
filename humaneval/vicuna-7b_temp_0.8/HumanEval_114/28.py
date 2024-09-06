import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left = float('-inf')
    right = float('inf')
    curr = 0
    for i in range(len(nums)):
        curr = max(curr, nums[i])
        if i == len(nums) - 1:
            right = curr
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        if nums[i] < curr:
            curr = nums[i]
        else:
            sub_sum = curr - nums[i] + nums[i + 1]
            if sub_sum < left:
                left = sub_sum
    return left
