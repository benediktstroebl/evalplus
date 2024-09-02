import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    cur_sum = 0
    best_sum = math.inf

    for num in nums:
        cur_sum += num
        best_sum = min(cur_sum, best_sum)

        if cur_sum < 0:
            cur_sum = 0

    return best_sum
