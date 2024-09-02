import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def dfs(nums, i, j):
        if i < 0 or j < 0:
            return 0
        if i == j:
            return nums[i]
        for k in range(max(i, j - 1), min(i + 1, j) + 1):
            dfs(nums, i, k)
            dfs(nums, k + 1, j)
            return nums[i] + nums[k + 1]

    return dfs(nums, 0, 0)

nums = [int(x) for x in input().split()]
result = minSubArraySum(nums)
