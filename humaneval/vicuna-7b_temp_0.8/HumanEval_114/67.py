import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def dfs(nums, low, high):
        if low == high:
            return 0
        mid = (low + high) // 2
        if nums[mid] == 0:
            return dfs(nums, low, mid) + dfs(nums, mid+1, high)
        if nums[mid] < 0:
            return -1
        return dfs(nums, low, mid)
    return dfs(nums, 0, len(nums) - 1)
