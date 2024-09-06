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

    for i, n in enumerate(nums):
        current_sum = current_sum + n
        if i == 0:
            min_sum = current_sum
        else:
            min_sum = min(min_sum, current_sum)
        current_sum = min(current_sum, 0)

    return min_sum
