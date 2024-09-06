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
    min_sum = nums[0]
    i = 0
    j = 0

    while j < n:
        min_sum = min(nums[j], min_sum)
        min_sum += nums[j]
        while i < j and min_sum >= 0:
            min_sum = min_sum - nums[i]
            i += 1

        j += 1

    if min_sum < 0:
        return 0
    else:
        return min_sum

