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
    cur_sum = 0
    for num in nums:
        cur_sum += num
        while cur_sum >= min_sum:
            cur_sum -= nums[nums.index(min(nums))]
        min_sum = min(min_sum, cur_sum)
    return min_sum
