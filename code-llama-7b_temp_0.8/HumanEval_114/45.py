import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # # MY SOLUTION
    # min_sum = math.inf
    # start, end = 0, len(nums) - 1
    # while start < end:
    #     if nums[start] + nums[end] < min_sum:
    #         min_sum = nums[start] + nums[end]
    #     elif nums[start] + nums[end] >= min_sum:
    #         end -= 1
    # return min_sum

    # # LEETCODE SOLUTION
    min_sum = math.inf
    min_sum_start = 0
    min_sum_end = 0
    start = 0
    end = 0
    while end < len(nums):
        sum_ = sum(nums[start:end+1])
        if sum_ < min_sum:
            min_sum = sum_
            min_sum_start = start
            min_sum_end = end
        if start < end:
            end += 1
        else:
            start += 1
            end = start
    return min_sum, min_sum_start, min_sum_end


