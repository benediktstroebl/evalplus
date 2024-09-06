import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    l, r = 0, 1
    total = 0
    smallest = float('inf')
    while r < len(nums) and l < len(nums):
        if total < 0:
            total = 0
            while r < len(nums) and total < 0:
                total += nums[r]
                r += 1
        else:
            smallest = min(total, smallest)
            total -= nums[l]
            l += 1
    return min(smallest, total) + min(nums)
