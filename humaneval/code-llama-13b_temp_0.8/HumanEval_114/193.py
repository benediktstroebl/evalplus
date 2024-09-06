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
        return None

    curr_sum = 0
    smallest_sum = math.inf
    for num in nums:
        curr_sum += num
        smallest_sum = min(curr_sum, smallest_sum)
        if curr_sum < 0:
            curr_sum = 0
    return smallest_sum

