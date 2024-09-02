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
    else:
        min_sum = math.inf
        for i in range(len(nums)):
            if nums[i] == -math.inf:
                min_sum = -math.inf
                break
            else:
                min_sum = min(nums[i], min_sum + nums[i])

        return
