import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = sum(nums)
    left = 0
    right = 0
    while right < len(nums):
        while left < len(nums):
            if (minSum == sum(nums[left:right+1])):
                break
            else:
                minSum = min(minSum, sum(nums[left:right+1]))
                left += 1
        right += 1
    return minSum
