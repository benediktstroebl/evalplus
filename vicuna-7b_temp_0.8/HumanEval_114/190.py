import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Create a default dictionary to store the sum of each subarray
    sums = {}
    for num in nums:
        if num in sums:
            sums[num] += 1
        else:
            sums[num] = 1

    # Find the minimum sum of any non-empty subarray
    min_sum = float('inf')
    for key, value in sums.items():
        if value > 0:
            min_sum = min(min_sum, value)

    return min_sum
