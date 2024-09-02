import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def dfs(i, j):
        if i == len(nums) or j == len(nums[0]):
            return nums[i][j]
        for k in range(i, len(nums)):
            dfs(i, nums[k][j])
            dfs(k + 1, j)
        return 0

    min_sum = float('inf')
    for i in range(0, len(nums), 2):
        for j in range(i, len(nums)):
            if nums[i][j] > 0:
                min_sum = min(min_sum, dfs(i, j))
    return min_sum

nums = [2, 3, 4, 1, 2, 4]
result = minSubArraySum(nums)
