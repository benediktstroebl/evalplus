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

    length = len(nums)

    current, global_min = 0, float('inf')
    for i, num in enumerate(nums):
        current += num
        if current == global_min:
            global_min = min(global_min, current)
        elif current < global_min:
            global_min = current

    return global_min
