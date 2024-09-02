import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    sum = math.inf
    cur_sum = 0
    for x in nums:
        cur_sum += x
        if cur_sum < sum:
            sum = cur_sum
        if cur_sum > 0:
            cur_sum = 0
    return sum if sum != math.inf else 0
