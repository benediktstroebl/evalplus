import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    for i in range(len(nums)):
        for j in range(i):
            # This condition check if the subarray sum is less than the current subarray sum
            if sum(nums[:i+j+1]) >= sum(nums[:i+j]):
                nums[:i+j+1] = nums[:i+j+1] - nums[i]
                nums = nums[:i] + nums[i+1:]
                break
    return sum(nums)