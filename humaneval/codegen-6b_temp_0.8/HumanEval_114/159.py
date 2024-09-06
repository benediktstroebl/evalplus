import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    S = sum(nums)
    if S == 0:
        return 0

    i = 0
    while i < len(nums):
        if i == 0:
            current_min = nums[i]
            current_min_val = nums[i]
        else:
            if current_min_val < 0:
                current_min_val = nums[i]
            current_min = min(current_min_val, current_min)
            current_min_val = current_min_val + nums[i]
            if current_min_val < 0:
                current_min_val = nums[i]

        i += 1

    return current_min

