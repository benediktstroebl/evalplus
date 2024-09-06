import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) < 1:
        return math.inf

    min_sum = math.inf
    total_sum = 0
    for index, value in enumerate(nums):
        total_sum += value

        if total_sum < min_sum:
            min_sum = total_sum

        if total_sum - min_sum >= 0:
            total_sum -= nums[index - 1]

    return min_sum


