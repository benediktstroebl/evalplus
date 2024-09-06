import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_subarray_sum = math.inf
    left = 0
    right = 0

    total = nums[left]

    while right < len(nums):
        if total > min_subarray_sum:
            break

        total += nums[right]
        min_subarray_sum = min(min_subarray_sum, total)
        right += 1

    return min_subarray_sum

