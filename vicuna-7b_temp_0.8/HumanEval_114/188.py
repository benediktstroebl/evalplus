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
    left, right = 1, len(nums)
    while left <= right:
        mid = (left + right) // 2
        sum = mid
        for i in range(mid):
            sum -= nums[i]
        if sum >= 0:
            return sum
        right = mid - 1
    return left
