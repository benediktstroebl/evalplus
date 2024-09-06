import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sub_array = []
    total_sum = 0

    for i in range(len(nums)):
        total_sum += nums[i]
        sub_array.append(total_sum)

    min_total = float('inf')

    for i in range(len(nums)):
        if(min_total > sub_array[i]):
            min_total = sub_array[i]

    return min_total

