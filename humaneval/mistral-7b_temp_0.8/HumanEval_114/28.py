import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Write your code here
    min_sum = math.inf
    window_sum = 0

    for i in range(len(nums)):
        window_sum += nums[i]

        while window_sum >= 0:
            min_sum = min(min_sum, window_sum)
            window_sum -= nums[i-len(nums)]

    return min_sum if min_sum != math.inf else 0
