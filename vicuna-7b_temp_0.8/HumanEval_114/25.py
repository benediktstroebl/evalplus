import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 0, max(nums)
    while left < right:
        mid = (left + right) // 2
        if mid == 0:
            right = mid + 1
            continue
        if nums[left] < 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left = mid + 1
            continue
        sum = left + mid
        while mid < right and nums[mid] == nums[mid - 1] + 1:
            mid += 1
            sum -= mid
        if sum >= mid:
            return sum
        left = mid + 1
    return left + 1
