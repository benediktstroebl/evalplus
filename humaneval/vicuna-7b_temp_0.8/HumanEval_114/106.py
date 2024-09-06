import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def dfs(i, j, nums):
        if i == len(nums) or j == len(nums[0]):
            return
        nums[i][j] = min(nums[i][j], nums[i][j+1])
        dfs(i+1, j, nums)
        dfs(i-1, j, nums)
        dfs(i, j+1, nums)
        dfs(i, j-1, nums)

    for i in range(len(nums)):
        for j in range(len(nums[0])):
            dfs(i, j, nums)

    return sum(nums)
