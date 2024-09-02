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
        if i == len(nums) or j == len(nums[0]):
            return nums[i:j+1]
        if nums[i] == nums[j]:
            dfs(nums, i+1, j)
            dfs(nums, i, j+1)
        else:
            dfs(nums, i+1, j)
            dfs(nums, i, j+1)
            return min(dfs(nums, i+1, j), dfs(nums, i, j+1))

    return dfs(nums, 0, 0)
