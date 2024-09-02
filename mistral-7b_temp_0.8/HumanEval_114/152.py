import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    min_sum = math.inf
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            s = sum(nums[i:j+1])
            if s < min_sum:
                min_sum = s
    return min_sum

