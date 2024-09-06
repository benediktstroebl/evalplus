import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums is None or len(nums) == 0:
        return None

    result = nums[0]
    minSubArray = 0

    for i in range(0, len(nums)):
        minSubArray += nums[i]

        if minSubArray < result:
            result = minSubArray

        while minSubArray >= nums[i]:
            minSubArray -= nums[i - 1]

    return result
