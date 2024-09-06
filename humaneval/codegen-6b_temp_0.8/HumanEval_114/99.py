import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    min_sum = 0
    i = 0
    while i < len(nums):
        curr_sum = 0
        j = i
        while j < len(nums):
            curr_sum += nums[j]
            if curr_sum < 0:
                break
            min_sum = min(min_sum, curr_sum)
            j += 1
        i += 1
    return min_sum

