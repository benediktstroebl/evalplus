import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums == None or len(nums) == 0:
        return 0

    sum = 0
    min_sum = math.inf
    min_start = 0
    min_end = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum < min_sum:
            min_sum = sum
            min_start = 0
            min_end = i
        elif sum > min_sum:
            sum = 0
            min_start = i + 1
            min_end = i + 1

    return nums[min_start:min_end + 1]
