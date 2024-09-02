import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    """
    # Initial thought: O(n^2)
    min_sum = 1e8
    for i in range(len(nums)):
        sub_sum = 0
        for j in range(i, len(nums)):
            sub_sum += nums[j]
            if sub_sum < min_sum:
                min_sum = sub_sum
    return min_sum
    """
    # Better solution: O(n)
    min_sum = 1e8
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > 0:
            current_sum = 0
    return min_sum
