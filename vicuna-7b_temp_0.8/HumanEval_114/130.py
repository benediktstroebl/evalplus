import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left = 1000000000
    right = -1000000000
    max_sum = max(nums)
    for i in range(len(nums)):
        for j in range(i):
            sum = nums[i] + nums[j]
            if sum < 0:
                return -1
            if sum == 0:
                continue
            if sum >= max_sum:
                continue
            if sum < left or (sum == left and nums[i] > left):
                left = sum
            if sum < right or (sum == right and nums[i] < right):
                right = sum
    return left
