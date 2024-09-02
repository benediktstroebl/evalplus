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
        return
    min_sum = math.inf
    start = 0
    end = 0
    curr_sum = 0
    while end < len(nums):
        curr_sum += nums[end]
        end += 1
        while curr_sum >= 0:
            min_sum = min(min_sum, curr_sum)
            curr_sum -= nums[start]
            start += 1
    return min_sum

