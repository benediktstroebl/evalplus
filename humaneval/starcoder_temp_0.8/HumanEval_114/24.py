import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0

    sum_min = sum_max = nums[0]
    sum_now = 0

    for i in range(len(nums)):
        sum_now += nums[i]
        if sum_now < sum_min:
            sum_min = sum_now

        if sum_now > sum_max:
            sum_max = sum_now

    return sum_min if sum_min < 0 else sum_max
