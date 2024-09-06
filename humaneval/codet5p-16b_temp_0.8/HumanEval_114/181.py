import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    n = len(nums)
    max_subarray = math.inf
    for start in range(n):
        temp_sum = 0
        for end in range(start, n):
            temp_sum += nums[end]
            if temp_sum < max_subarray:
                max_subarray = temp_sum
    return max_subarray
