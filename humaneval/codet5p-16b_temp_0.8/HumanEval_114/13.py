import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    max_so_far = math.inf
    curr_sum = 0
    start = 0
    for end in range(len(nums)):
        curr_sum += nums[end]
        while curr_sum >= max_so_far:
            max_so_far = curr_sum
            start = start + 1
            curr_sum = curr_sum - nums[start]
    return max_so_far
