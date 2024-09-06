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
    left = 0
    right = 0
    min_sum = math.inf
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
        while curr_sum < 0:
            curr_sum -= nums[left]
            left += 1
    return min_sum
