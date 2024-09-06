import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 0, len(nums)-1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[left] + nums[mid] < nums[mid] + nums[right]:
            left = mid + 1
        else:
            right = mid - 1
            
    return nums[left] + nums[left+1] + nums[left+2]
