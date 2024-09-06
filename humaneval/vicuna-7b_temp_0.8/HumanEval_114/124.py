import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 1, nums[0]
    for i in range(1, len(nums)):
        if nums[i] < nums[left]:
            left = i
        else:
            right = i
    ans = nums[left]+nums[right]
    for i in range(left, len(nums)):
        if nums[i] < nums[left]:
            ans = min(ans, nums[left]-nums[i]+nums[i+1])
    return ans
