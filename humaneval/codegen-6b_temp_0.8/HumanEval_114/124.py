import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    """
    if not nums:
        return 0
    min_sum = sum(nums)
    min_start = 0
    p_sum = 0
    for i in range(len(nums)):
        p_sum += nums[i]
        while p_sum < 0:
            p_sum -= nums[min_start]
            min_start += 1
        if p_sum < min_sum:
            min_sum = p_sum
    return min_sum
    """
    """
    if not nums:
        return 0
    min_sum = sum(nums)
    min_start = 0
    p_sum = 0
    for i in range(len(nums)):
        p_sum += nums[i]
        while p_sum < 0:
            p_sum -= nums[min_start]
            min_start += 1
        if p_sum < min_sum:
            min_sum = p_sum
    return min_sum
    """
    """
    # if not nums:
    #     return 0
    # min_sum = sum(nums)
    # min_start = 0
    # p_sum = 0
    # for i in range(len(nums)):
    #     p_sum += nums[i]
    #     while p_sum < 0:
    #         p_sum -= nums[min_start]
    #         min_start += 1
    #     if p_sum < min_sum:
    #         min_sum = p_sum
    # return min_sum
    """
    if not nums:
        return 0
    min_sum = sum(nums)
    min_start = 0
    p_sum = 0
    for i in range(len(nums)):
        if p_sum < 0:
            p_sum = 0
            min_start = i
        p_sum += nums[i]
        if p_sum < min_sum:
            min_sum = p_sum
    if p_sum > 0:
        return min_sum
    return min_sum - nums[min_