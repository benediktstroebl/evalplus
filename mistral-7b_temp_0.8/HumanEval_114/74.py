import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    nums = [4,2,3,0]
    if len(nums) == 1:
        return nums[0]

    min_sub_array = nums[0]
    window_sum = 0

    for i in range(1, len(nums)):
        window_sum += nums[i]

        while window_sum >= min_sub_array:
            window_sum -= nums[i-1]

        if window_sum < min_sub_array:
            min_sub_array = window_sum

    return min_sub_array
