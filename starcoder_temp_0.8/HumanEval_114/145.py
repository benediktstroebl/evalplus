import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums or len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]

    result = float("inf")

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            temp_sum = 0
            for k in range(i, j + 1):
                temp_sum += nums[k]

            if temp_sum < result:
                result = temp_sum

    return result
