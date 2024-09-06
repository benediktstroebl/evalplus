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
        return 0
    minSum = nums[0]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            if nums[i:j] == sorted(nums[i:j]):
                if minSum == None or minSum > sum(nums[i:j]):
                    minSum = sum(nums[i:j])
    return minSum
