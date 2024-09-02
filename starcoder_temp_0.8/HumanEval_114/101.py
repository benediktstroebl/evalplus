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
        subArraySum = min(nums)
        for i in range(len(nums)):
            subArraySum = min(subArraySum, nums[i])
            for j in range(i+1, len(nums)):
                subArraySum += nums[j]
                if subArraySum > min(nums):
                    return subArraySum
        return subArraySum

