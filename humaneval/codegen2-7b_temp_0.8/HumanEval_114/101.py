import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum, min_sum = nums[0], nums[0]
    for i in range(1, len(nums)):
        sum += nums[i]
        if sum < nums[i]:
            min_sum = min(sum, min_sum)
        else:
            sum -= nums[i-1]
    return min_sum
