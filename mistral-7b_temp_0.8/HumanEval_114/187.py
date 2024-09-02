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
    min_sum_start = 0
    min_sum_end = 0
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum > min_sum:
            min_sum = sum
            min_sum_start = min_sum_end
            min_sum_end = i

        if sum < 0:
            sum = 0
            min_sum_end = i

    print("{} {} {}".format(nums, min_sum, min_sum_start, min_sum_end))

