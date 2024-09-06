import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    for i in range(len(nums)-1):
        j = i+1
        while j < len(nums):
            nums[i:j+1] = [nums[i]+nums[j] for nums[j] in nums[j+1:]]
            sum = reduce(lambda x, y: x+y, nums[i:j])
            if sum < nums[i]:
                minSum = sum
    return minSum
