import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum_of_subarrays = []
    subarrays = []
    min_subarrays = math.inf
    min_index = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            subarrays.append(nums[i:j + 1])
    for i in range(0, len(subarrays)):
        sum_of_subarrays.append(sum(subarrays[i]))
        if sum_of_subarrays[i] < min_subarrays:
            min_subarrays = sum_of_subarrays[i]
            min_index = i
    return min_index

