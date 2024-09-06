import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        minSum = 10**10
        left = 0
        right = 0
        while right < len(nums):
            while right - left + 1 > 1 and nums[left] + nums[right] > nums[right]:
                left += 1
            minSum = min(minSum, nums[left] + sum(nums[left+1:right+1]))
            right += 1
        return minSum
