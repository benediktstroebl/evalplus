import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Caching
    cache = {}
    cache[0] = 0
    cache[1] = 0
    cache[2] = nums[1]
    cache[3] = nums[1] + nums[2]

    # Using Fibonacci Series
    # Adding up the sums of the first two sub-arrays
    sum1 = sum(nums[0:2])
    sum2 = sum(nums[1:3])
    # The first element of the series of the sums of the sub-arrays
    sum3 = sum1 + sum2

    # Caching the sums of the first two sub-arrays
    cache[4] = sum3

    # The next element in the series will be the sum of the last two sums in the series
    # minus the first two elements in the series
    sum4 = sum3 - (cache[2] - cache[1])

    # Continuing this process until we reach the length of the array - 2
    for i in range(4, len(nums) - 2):
        cache[i + 1] = sum4
        sum4 = sum4 - (cache[i - 1] - cache[i - 2])

    # This dictionary contains all the sums of the sub-arrays
    return min(cache.values())
