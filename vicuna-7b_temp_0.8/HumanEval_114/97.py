import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # sort the nums
    nums = sorted(nums)
    
    # if the array is empty, return 0
    if not nums:
        return 0
    
    # initialize the sum and the leftmost index of the current sub-array
    sum = nums[0]
    leftmost = 0
    
    # find the rightmost index of the sub-array
    for i in range(len(nums) - 1):
        sum += nums[i]
        if nums[i] <= sum / 2:
            break
    
    # add the leftmost num to the sub-array and update the sum
    sub_array = [nums[leftmost], sum]
    sum += leftmost
    
    # recursively find the minimum sum of any non-empty sub-array of the remaining nums
    return minSubArraySum(nums[leftmost:]) + sub_array[1]
