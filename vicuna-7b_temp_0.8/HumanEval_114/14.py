import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left = 0
    right = max(nums)
    while right - left > 1:
        mid = (left + right) // 2
        if nums[left] <= mid:
            if mid not in nums:
                nums.append(mid)
                left = mid + 1
            elif nums[mid] < mid:
                nums[left], nums[mid] = mid, nums[left]
                left += 1
        else:
            right = mid
    return sum(nums)
