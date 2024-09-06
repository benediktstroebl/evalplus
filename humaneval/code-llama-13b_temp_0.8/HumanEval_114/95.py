import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # min subarray problem
    if len(nums) == 1:
        return nums[0]
    # using dynamic programming, we keep track of a subarray with the minimum sum
    current_sum = 0
    max_sum = float('-inf')
    for num in nums:
        current_sum += num
        if current_sum < max_sum:
            max_sum = current_sum
        if current_sum > 0:
            current_sum = 0
    return max_sum
