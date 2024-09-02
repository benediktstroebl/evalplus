import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Check if nums is empty or not
    if not nums:
        return -1
    
    # Check if nums is a list of integers in range [0, min_sum)
    if any(num < 0 for num in nums):
        return -1
    
    # Sort nums in ascending order
    nums = sorted(nums)
    
    # Initialize min_sum and curr_sum
    min_sum = nums[-1]
    curr_sum = nums[-1]
    
    # Traverse through the array, starting from the second element
    for i in range(1, len(nums)):
        curr_sum += nums[i]
        if curr_sum > min_sum:
            min_sum = curr_sum
    
    return min_sum