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
    right = n
    min_sum = math.inf
    min_index = 0
    
    while left < right:
        while left < right and nums[left] <= 0:
            left += 1
        while left < right and nums[right] >= 0:
            right -= 1
        if left < right:
            sum = nums[left] + nums[right]
            if sum < min_sum or (sum == min_sum and nums[left] + nums[right] != nums[left] + right):
                min_sum = sum
                min_index = left
    
    return nums[min_index], min_sum
