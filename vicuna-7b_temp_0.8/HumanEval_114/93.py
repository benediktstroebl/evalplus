import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def dfs(nums, start, sum):
        if start == len(nums):
            return sum
        for i in range(start, len(nums)):
            if nums[start] + nums[i] < nums[start+1]:
                dfs(nums, i, sum + nums[start])
        return sum
    
    for i in range(len(nums)):
        if nums[i] == 0:
            return dfs(nums, 0, 0)
    return dfs(nums, 0, 0)

nums = [2, 3, 4, 1, 2, 4]
result = minSubArraySum(nums)
print(result)
