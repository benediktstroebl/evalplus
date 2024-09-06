import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) < 2:
        return sum(nums)
    l_sum = nums[0]
    r_sum = nums[1]
    if r_sum > l_sum:
        min_sum = r_sum
    else:
        min_sum = l_sum
    for i in range(2, len(nums)):
        if l_sum + nums[i] - nums[i - 2] < min_sum:
            min_sum = l_sum + nums[i] - nums[i - 2]
        l_sum += nums[i]
        if l_sum < r_sum:
            r_sum = l_sum
        elif r_sum < min_sum:
            min_sum = r_sum
    return min_sum
