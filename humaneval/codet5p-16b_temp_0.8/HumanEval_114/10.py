import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 1:
        return nums[0]

    current_sum = min_sum = math.inf
    start_index = end_index = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum < min_sum:
            min_sum = current_sum
            end_index = i + 1

    return min_sum

