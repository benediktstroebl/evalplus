import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = sum(nums)
    curr_sum = 0
    start = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum < 0:
            start = i + 1
            curr_sum = 0
        elif curr_sum < min_sum:
            min_sum = curr_sum

    curr_sum = 0
    end = len(nums) - 1
    for i in reversed(range(len(nums))):
        curr_sum += nums[i]
        if curr_sum < 0:
            end = i - 1
            curr_sum = 0
        elif curr_sum < min_sum:
            min_sum = curr_sum

    return min_sum if min_sum != sum(nums) else min(nums[start:end+1])

