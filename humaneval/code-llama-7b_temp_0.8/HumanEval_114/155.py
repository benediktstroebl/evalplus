import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minimum_sub_array_sum = math.inf

    running_min_sum = 0
    for num in nums:
        running_min_sum += num
        if running_min_sum < minimum_sub_array_sum:
            minimum_sub_array_sum = running_min_sum

        if running_min_sum <= 0:
            running_min_sum = 0

    return minimum_sub_array_sum
