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
    else:
        prev_sum = len(nums) * 10 ** 9
        curr_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            curr_sum += nums[i]
            if prev_sum > curr_sum:
                prev_sum = curr_sum

        return prev_sum

