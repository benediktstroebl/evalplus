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

    sum = 0
    min_sum = math.inf
    window_start = 0

    for window_end in range(len(nums)):
        sum += nums[window_end]
        while sum >= 0:
            min_sum = min(min_sum, sum)
            window_start += 1
            if window_start >= window_end:
                break
            sum -= nums[window_start]

    return min_sum if min_sum!= math.inf else 0
