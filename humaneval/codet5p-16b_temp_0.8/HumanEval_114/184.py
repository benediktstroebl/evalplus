import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_sum = math.inf
    total = 0
    for i in range(len(nums)):
        total = nums[i]
        if i + 1 >= len(nums):
            min_sum = min(total, min_sum)
        else:
            total = total + nums[i+1]
            if total < min_sum:
                min_sum = total
    return min_sum
