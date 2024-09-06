import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return -1
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        if mid in nums:
            j = mid
            while j > 0 and nums[j-1] >= nums[j]:
                j = j - 1
            while j < len(nums) and nums[j] <= nums[mid]:
                j = j + 1
            if j > 0:
                right = mid - 1
            else:
                left = mid + 1
        else:
            right = mid
    return left + right
