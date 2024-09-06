import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    current_sum = float('inf')
    sums = sum(nums)
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            current_sum = min(current_sum, math.fsum(nums[i:j+1]))
    return current_sum if current_sum!= float('inf') else None


