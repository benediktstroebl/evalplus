import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    m, n = len(nums), len(nums[0])
    curr_sum = nums[0]
    curr_index = 0
    for i in range(1, m):
        for j in range(1, n):
            if nums[i] >= 0 and nums[j] >= 0 and curr_sum + nums[i] <= nums[j]:
                curr_sum += nums[i]
                curr_index = j
        else:
            curr_sum += nums[i]
            curr_index = i
    return curr_sum
