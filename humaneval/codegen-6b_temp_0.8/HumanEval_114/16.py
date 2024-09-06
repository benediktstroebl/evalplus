import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    assert type(nums) == list
    assert len(nums) > 0
    result = nums[0]
    min_sum = result
    for num in nums:
        result = max(result + num, 0)
        min_sum = min(min_sum, result)
    return min_sum
