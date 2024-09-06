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
    if len(nums) == 1:
        return nums[0]
    left, right, minSum = 0, 1, 0
    while right <= len(nums):
        print left, right
        tempSum = sum(nums[left:right])
        if tempSum < minSum or minSum == 0:
            minSum = tempSum
        left += 1
        right += 1
    return minSum
