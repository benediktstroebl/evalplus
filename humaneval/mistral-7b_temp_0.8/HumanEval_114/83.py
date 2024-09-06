import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    nums_len = len(nums)
    min_sum = float('inf')
    start_index = 0
    end_index = 0
    while(end_index < nums_len):
        sum_ = 0
        while(end_index < nums_len and sum_ < min_sum):
            sum_ += nums[end_index]
            end_index += 1
        while(start_index <= end_index - 1 and sum_ < min_sum):
            sum_ -= nums[start_index]
            start_index += 1
        if sum_ < min_sum:
            min_sum = sum_
            min_index = start_index
            max_index = end_index
    return nums[min_index:max_index+1]

