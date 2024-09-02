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
    
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        
        if mid == 0:
            if nums[left] + nums[mid] <= nums[right]:
                return nums[left] + nums[mid]
        elif nums[left] + nums[mid] > nums[right]:
            right = mid
        else:
            left = mid + 1

    return -1
