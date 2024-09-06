import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    if n == 0:
        return 0

    for i in range(n):
        if nums[i] == nums[i - 1]:
            nums[i] = 0
            nums[i - 1] = 0

    sum = 0
    index = 0
    for i in range(n):
        sum += nums[i]
        if sum < 0:
            sum = 0
            index = i + 1

    return sum

