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
        if i + 1 == len(nums):
            return
        if j + 1 == len(nums):
            return
        num = nums[i][j]
        if num > 0:
            dfs(nums, i + 1, j - 1)
            dfs(nums, i + 1, j)
        dfs(nums, i + 1, j + 1)

    min_sum = float('inf')
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            dfs(nums, i, j)
            if sum(nums[i:i+j]) < min_sum:
                min_sum = sum(nums[i:i+j])
    return min_sum
