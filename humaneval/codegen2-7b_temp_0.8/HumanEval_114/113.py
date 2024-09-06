import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left = 0
    sum = 0
    for right, num in enumerate(nums):
        sum += num
        while sum >= nums[left]:
            sum -= nums[left]
            left += 1
    if left == len(nums):
        return nums[left-1]
    else:
        return -1
