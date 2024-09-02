import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    m = len(nums)
    if m == 0:
        return 0
    ans = nums[0]
    for i in range(1, m):
        if nums[i] < nums[i-1]:
            for j in range(i+1, m):
                nums[j] -= nums[i]
            ans = max(ans, nums[i-1]+nums[i])
    return ans
