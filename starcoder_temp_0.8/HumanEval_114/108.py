import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # O(n) time, O(1) space
    # This method uses Kadane's algorithm for the same problem.
    min_so_far = None
    curr_sum = 0
    for x in nums:
        curr_sum += x
        min_so_far = curr_sum if min_so_far is None or min_so_far > curr_sum else min_so_far
        if curr_sum < 0:
            curr_sum = 0
    return min_so_far
