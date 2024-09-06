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
    if len(nums) == 2:
        return math.min(nums[0],nums[1])

    minsum = math.inf
    for i in range(len(nums)):
        if i == 0:
            current_sum = nums[0]
            continue
        current_sum = current_sum + nums[i]
        if current_sum < minsum:
            minsum = current_sum
        if current_sum > minsum:
            current_sum = 0
    return minsum

