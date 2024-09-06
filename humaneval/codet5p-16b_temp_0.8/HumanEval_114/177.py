import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    result = math.inf
    total = 0
    start = 0
    for end, num in enumerate(nums):
        total += num
        if total < nums[start]:
            total = num
            start = end
        if total >= nums[start]:
            result = min(result, total - nums[start])
    return result if result!= math.inf else 0
