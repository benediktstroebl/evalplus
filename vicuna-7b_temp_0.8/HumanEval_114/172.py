import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 0, 0
    for i in range(len(nums)):
        if i == 0 or nums[i] < nums[i-1]:
            right = i
            while right-left >= 2:
                sum = left + right
                if sum in nums:
                    return sum
                right--
                left += 1
    return 0
