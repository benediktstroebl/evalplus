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
        return None
    min_sum = nums[0]
    sum_arr = [nums[0]]
    for i in range(1, len(nums)):
        sum_arr.append(sum_arr[i - 1] + nums[i])
        min_sum = min(min_sum, sum_arr[i])
    return min_sum
