import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # initialize
    if len(nums) == 1:
        return nums[0]
    min_sum = float('inf')
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        while current_sum >= 0:
            if min_sum > current_sum:
                min_sum = current_sum
            current_sum -= nums[i]
            i -= 1
    return min_sum
