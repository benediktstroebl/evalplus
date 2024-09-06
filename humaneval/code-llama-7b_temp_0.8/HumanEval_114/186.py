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

    max_sum = nums[0]
    min_sum = nums[0]
    curr_sum = 0

    for num in nums[1:]:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        min_sum = min(min_sum, curr_sum)

    return min(min_sum, max_sum)
