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
    else:
        s, e, c = 0, 0, 0
        c = nums[0]
        i = 1
        while s < len(nums):
            while e < len(nums):
                if c < sum(nums[s:e]):
                    c = sum(nums[s:e])
                e += 1
            s += 1
            e = s
            c = 0

    return c

