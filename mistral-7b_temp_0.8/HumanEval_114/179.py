import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # min_sum = nums[0]
    # for i in range(1, len(nums)):
    #     if nums[i] < min_sum:
    #         min_sum = nums[i]
    # return min_sum

    # Solution2: sliding window
    min_sum = nums[0]
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        min_sum = min(min_sum, s)
        if i >= 1:
            s = s - nums[i - 1]
    return min_sum
