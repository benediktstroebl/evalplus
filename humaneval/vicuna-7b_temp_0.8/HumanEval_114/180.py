import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    nums = list(nums)
    left, right = 1, max(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[left] <= mid:
            left += 1
        else:
            right = mid
    result = nums[left]
    for i in range(left, len(nums)):
        if nums[i] > result:
            result = math.inf
            start = i
    return result
