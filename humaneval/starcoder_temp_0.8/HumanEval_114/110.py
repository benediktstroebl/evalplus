import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_so_far = sys.maxsize
    current_sum = 0
    for num in nums:
        current_sum += num
        min_so_far = min(min_so_far, current_sum)
        if current_sum < 0:
            current_sum = 0
    return min_so_far if min_so_far!= sys.maxsize else 0
