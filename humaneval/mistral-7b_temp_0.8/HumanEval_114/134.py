import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_sum = nums[0]
    start_index = 0
    end_index = 0

    while end_index < len(nums) - 1:
        if nums[end_index] > 0:
            min_sum += nums[end_index]
            end_index += 1
        else:
            min_sum -= nums[start_index]
            start_index += 1
            end_index += 1

    print(min_sum)

