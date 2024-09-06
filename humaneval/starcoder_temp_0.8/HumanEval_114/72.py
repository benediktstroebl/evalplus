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
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    print(nums)
    total = nums[-1]
    print(total)
    for i in range(1, len(nums)):
        if total - nums[i] < 0:
            return nums[i]
    return total
