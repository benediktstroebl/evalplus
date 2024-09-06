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
    sum = 0
    n = len(nums)
    for j in range(n):
        sum += nums[j]
        if sum < min_sum:
            min_sum = sum
        if sum > 0 and j - i + 1 > min_sum:
            sum -= nums[i]
            i += 1

    return min_sum

