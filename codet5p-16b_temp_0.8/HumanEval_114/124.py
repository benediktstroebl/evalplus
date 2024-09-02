import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_sum = math.inf
    running_sum = 0
    left_index = 0
    for i in range(0, len(nums)):
        running_sum = running_sum + nums[i]
        while left_index < len(nums) and running_sum >= min_sum:
            min_sum = running_sum
            left_index = left_index + 1
            running_sum = running_sum - nums[left_index]
        if left_index == len(nums):
            break

    if running_sum < min_sum:
        min_sum = running_sum

    return min_sum

