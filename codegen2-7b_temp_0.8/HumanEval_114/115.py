import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    count = 0
    for num in nums:
        if count == 0:
            count += num
        else:
            count += num
            if count < 0:
                count = 0
    return count

