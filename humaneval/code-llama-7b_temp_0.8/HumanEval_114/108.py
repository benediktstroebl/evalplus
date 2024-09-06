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

    sum = nums[0]
    min_sum = math.inf

    for i in range(1, len(nums)):
        if nums[i] < 0:
            sum += nums[i]
        elif sum < 0:
            sum = nums[i]
        else:
            min_sum = min(min_sum, sum+nums[i])

    return min_sum
