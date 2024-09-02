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
    i = 0
    j = 0
    sum = 0

    while i < len(nums):
        sum += nums[i]

        while sum >= min_sum:
            min_sum = min(sum, min_sum)
            sum -= nums[j]
            j += 1

        i += 1
        sum += nums[i]

    return min_sum
