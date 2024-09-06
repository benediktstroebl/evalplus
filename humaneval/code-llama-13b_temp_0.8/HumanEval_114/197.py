import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total = math.inf
    sum = 0
    for num in nums:
        sum += num
        if total > sum:
            total = sum
        if sum > 0:
            sum = 0
        # print(total, sum)
    return total if total != math.inf else 0

