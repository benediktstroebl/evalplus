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

    min_so_far = math.inf
    current_sum = 0
    for current_num in nums:
        current_sum += current_num
        if current_sum < min_so_far:
            min_so_far = current_sum

    return min_so_far if min_so_far < math.inf else
