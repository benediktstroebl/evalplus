import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Precompute sums for the entire array
    sums = [0] * len(nums)
    sums[0] = nums[0]
    for i in range(1, len(nums)):
        sums[i] = sums[i-1] + nums[i]

    min_index = -1
    min_sum = float("inf")
    for i in range(len(nums)):
        if sums[i] >= 0:
            min_index = i
            min_sum = sums[i]
            break
    if min_index == -1:
        return min_sum

    for i in range(min_index+1, len(nums)):
        j = i
        while j < len(nums):
            if sums[j] - sums[i] == min_sum:
                return min_sum
            j = j+1
    return None
