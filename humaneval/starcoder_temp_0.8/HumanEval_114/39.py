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
        return 0

    cur_min = 0
    cur_sum = 0
    min_sum = math.inf

    for num in nums:
        cur_sum += num
        cur_min = min(cur_min, cur_sum)
        min_sum = min(min_sum, cur_sum)

        if cur_sum < 0:
            cur_sum = 0

    return min_sum
