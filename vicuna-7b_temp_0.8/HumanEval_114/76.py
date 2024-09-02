import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    left_sum = 0
    left_index = 0
    right_sum = nums[0]
    right_index = 1
    for i in range(1, n):
        if nums[i] < 0:
            left_sum = max(left_sum + nums[i], left_sum + nums[-1])
            right_sum = max(right_sum + nums[i], right_sum)
            left_index += 1
            right_index += 1
        else:
            if left_sum + nums[i] <= right_sum:
                right_sum = max(right_sum + nums[i], right_sum)
                right_index += 1
            else:
                left_sum = max(left_sum + nums[i], left_sum)
                left_index += 1
    return max(right_sum, left_sum)
