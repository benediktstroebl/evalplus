import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # init
    min_sum = math.inf
    cur_sum = 0
    # cur_sum + nums[0]
    for num in nums:
        cur_sum += num
        if min_sum > cur_sum:
            min_sum = cur_sum
        if cur_sum > 0:
            cur_sum = 0
    return min_sum if min_sum != math.inf else 0

