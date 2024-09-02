import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    ans = nums[0] # assume the first element is the minimum sum
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum < 0:
            curr_sum = 0
        else:
            if curr_sum < ans:
                ans = curr_sum
    return ans
