import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def dfs(nums, left, right):
        if right - left + 1 <= 0:
            return
        if left < 0 or right > len(nums):
            return
        if nums[left] == nums[right]:
            dfs(nums, left + 1, right - 1)
            dfs(nums, left + 1, right)
            dfs(nums, left + 1, right - 1)
        else:
            dfs(nums, left + 1, right)
    if not nums:
        return 0
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[left] + nums[right]:
            dfs(nums, left, mid)
            dfs(nums, mid + 1, right)
            dfs(nums, left, mid)
        else:
            dfs(nums, left, mid)
            dfs(nums, mid + 1, right)
    return nums[0]

nums = [int(input()) for i in range(input().strip().split())]
result = minSubArraySum(nums)
