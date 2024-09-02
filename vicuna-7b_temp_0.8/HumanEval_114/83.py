import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    nums.sort()
    curr_sum = nums[0]
    curr_index = 0
    for i in range(1, len(nums)):
        if nums[i] > curr_sum:
            curr_sum = nums[i]
            curr_index = i - 1
        elif nums[i] < curr_sum:
            curr_sum = curr_sum - nums[i]
            curr_index = i - 1
        else:
            curr_sum += nums[i]
    return curr_sum - nums[curr_index]
