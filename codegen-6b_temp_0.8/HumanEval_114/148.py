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

    left, right, min = 0, 0, math.inf

    while right < len(nums):
        if len(nums) - right == 1:
            return nums[right]

        while left <= right and sum(nums[left:right + 1]) < min:
            min = sum(nums[left:right + 1])
            left += 1

        right += 1
    return min

