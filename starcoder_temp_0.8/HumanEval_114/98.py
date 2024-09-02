import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    max_num = max(nums)
    min_sum = 0
    for i in range(len(nums)):
        cur_sum = nums[i]
        min_sum += cur_sum
        while cur_sum > max_num:
            cur_sum -= nums[i - (len(nums) - i)]
            min_sum += cur_sum
    return min_sum
