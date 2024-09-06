import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Keep track of min sum up to the current index
    sums = [float('inf') for _ in range(len(nums))]
    sums[0] = 0
    for i in range(1, len(nums)):
        sums[i] = sums[i-1] + nums[i]

    # Find min sum between the first and last index
    min_sum = float('inf')
    for i in range(1, len(sums)-1):
        sub_sum = sums[i-1] + sums[-1] - sums[i]
        min_sum = min(min_sum, sub_sum)

    return min_sum
