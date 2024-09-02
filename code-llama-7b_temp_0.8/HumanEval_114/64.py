import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    left = 0
    right = n-1
    min = math.inf
    ans = 0
    while left <= right:
        if nums[left] + nums[right] < min:
            min = nums[left] + nums[right]
        if nums[left] < nums[right]:
            ans = min
            left += 1
        else:
            right -= 1
    return ans
