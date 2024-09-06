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
    left = 0
    right = 0
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        while sum >= min_subarray:
            sum -= nums[left]
            left += 1
        min_subarray = min(min_subarray, sum)

    return min_subarray
