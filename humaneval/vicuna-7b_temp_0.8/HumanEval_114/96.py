import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def dfs(nums, left=0, right=len(nums)-1, sum=0):
        if right < left:
            return
        if right > left and nums[right] < nums[left]:
            return
        if sum + nums[left] <= sum:
            dfs(nums, left+1, right, sum+nums[left])
        elif sum + nums[left] > sum:
            dfs(nums, left+1, right, sum+nums[left])
        else:
            return
        dfs(nums, left+1, right, sum+nums[left])

    nums = list(nums)
    dfs(nums, 0, len(nums)-1)
    return sum
