import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 1, nums[0]
    for i in range(1, len(nums)):
        if nums[i] < left:
            left = nums[i]
        elif nums[i] > right:
            right = nums[i]
        else:
            j = 0
            while nums[i+j] >= left:
                j += 1
            sub = nums[i:i+j+1]
            if sum(sub) < subSum:
                subSum = sum(sub)
    return subSum