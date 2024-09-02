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
    if len(nums) == 1:
        return nums[0]

    minimum = math.inf
    sum = 0
    start = 0
    end = 0

    while end < len(nums):
        sum += nums[end]
        end += 1
        while sum >= 0:
            minimum = min(sum, minimum)
            if end == len(nums):
                break
            sum -= nums[start]
            start += 1

    return minimum


