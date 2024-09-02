import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_sum = math.inf
    sub_arr = []
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]
        sub_arr.append(curr_sum)

    for i in range(len(sub_arr)):
        min_sum = min(min_sum, sub_arr[i])

    print(min_sum)

