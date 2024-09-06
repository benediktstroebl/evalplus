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
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        # first try brute force
        current_sum = 0
        for x in range(len(nums)):
            current_sum += nums[x]
            if current_sum < 0:
                current_sum = 0
    # now try dynamic programming
