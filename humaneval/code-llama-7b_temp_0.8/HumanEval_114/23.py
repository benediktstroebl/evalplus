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

    total = sum(nums)
    subarray = nums

    # Find the min sum of subarrays
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            subarray = nums[i:j]
            subtotal = sum(subarray)
            total = min(total, subtotal)

    return total
