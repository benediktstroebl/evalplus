import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    result = float('inf')
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        # if the sum of the current window exceeds the limit, we will narrow down the window
        while current_sum > result:
            current_sum -= nums[i-result]
            i -= result
        result = min(result, current_sum)
    return result
