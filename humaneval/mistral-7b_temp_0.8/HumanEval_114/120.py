import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    min_sum = 1e9
    length = len(nums)
    # i = 0
    # for i in range(length):
    #     s = 0
    #     j = i
    #     while j < length:
    #         s += nums[j]
    #         if s < min_sum:
    #             min_sum = s
    #         j += 1
    #     if s < min_sum:
    #         min_sum = s
    #         i = j - 1
    start = 0
    end = 0
    min_sum = 1e9
    s = 0
    while end < length:
        s += nums[end]
        if s < min_sum:
            min_sum = s
        while s > nums[start]:
            s -= nums[start]
            start += 1
        end += 1
    return min_sum

