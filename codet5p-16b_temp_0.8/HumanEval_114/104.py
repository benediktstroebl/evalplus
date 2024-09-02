import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    length = len(nums)
    if len(nums) == 0:
        return 0
    
    total_sum = 0
    min_sum = math.inf
    start_idx = 0

    for i in range(length):
        total_sum += nums[i]

        while total_sum >= 0:
            min_sum = min(min_sum, total_sum)
            total_sum -= nums[start_idx]
            start_idx += 1

    return min_sum
