import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_subarray = math.inf
    total = 0
    for i, v in enumerate(nums):
        total += v

        if total > min_subarray:
            continue

        for j in range(i, len(nums)):
            total += nums[j]
            if total > min_subarray:
                continue

            min_subarray = min(min_subarray, total)

    return min_subarray
