import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums == []:
        return -1
    size = len(nums)
    min_sum = 0
    for i in range(size):
        current_sum = 0
        for j in range(i, size):
            current_sum += nums[j]
            if current_sum >= min_sum:
                min_sum = current_sum
        if current_sum < min_sum:
            min_sum = current_sum
