import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sums = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            sums[i] += nums[j]
    left = len(nums)
    while left > 0:
        right = 0
        while left > right:
            if sums[left-1] <= sums[right]:
                left -= 1
            else:
                right += 1
        left = right
    return sums[-1]
