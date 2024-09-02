import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = math.inf
    for i in range(len(nums)):
        local_sum = sum
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum < local_sum:
                local_sum = sum
        sum = local_sum
    return
