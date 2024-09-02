import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sub_sum = 0
    min_sum = math.inf
    left = 0
    for right in range(len(nums)):
        sub_sum += nums[right]
        while sub_sum >= min_sum:
            min_sum = min(min_sum, sub_sum)
            sub_sum -= nums[left]
            left += 1
    return min_sum
