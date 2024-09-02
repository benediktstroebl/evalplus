import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_sub_sum = math.inf
    current_sum = 0
    for i, n in enumerate(nums):
        current_sum += n
        if current_sum < min_sub_sum:
            min_sub_sum = current_sum
        while i + 1 < len(nums) and current_sum >= min_sub_sum:
            current_sum -= nums[i]
            i += 1
    return min_sub_sum
