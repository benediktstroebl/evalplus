import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Solution:
    # if the array is empty, return 0
    # otherwise, find the minimum sum of every subarray
    # return the minimum found
    if len(nums) == 0:
        return 0

    min_sum = nums[0]

    for i in range(len(nums)):
        cur_min = 0
        for j in range(i, len(nums)):
            cur_min += nums[j]
            if cur_min < min_sum:
                min_sum = cur_min

    return min_sum
