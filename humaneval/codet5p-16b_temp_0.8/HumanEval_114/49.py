import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0:
        return math.inf
    elif len(nums) == 1:
        return nums[0]
    else:
        current_min = math.inf
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total < current_min:
                current_min = total
            if total < 0:
                total = 0
        return current_min
