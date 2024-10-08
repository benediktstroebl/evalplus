import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Set initial values
    current_sum = 0
    min_sum = math.inf

    # Loop through array and update sums
    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        current_sum = max(current_sum, 0)

    return min_sum
