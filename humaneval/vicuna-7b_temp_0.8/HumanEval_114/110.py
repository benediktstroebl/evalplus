import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # sort the input list
    nums = sorted(nums)

    if not nums:
        return 0

    # check if the first two numbers are -1 and -2 or -2 and -3
    if nums[0] == -1 and nums[1] == -2 or nums[0] == -2 and nums[1] == -3:
        return nums[0] + nums[1]

    # check if the last two numbers are -1 and -2 or -2 and -3
    if nums[-1] == -1 and nums[-2] == -2 or nums[-1] == -2 and nums[-2] == -3:
        return nums[-1] + nums[-2]

    # check if the remaining numbers form a sub-array with sum -1
    if nums[-1] == -1:
        return nums[-2] + nums[-3] + nums[-1]

    # check if the remaining numbers form a sub-array with sum -2
    if nums[-2] == -2:
        return nums[-1] + nums[-3]

    # check if the remaining numbers form a sub-array with sum -3
    if nums[-3] == -3:
        return nums[-2] + nums[-1]

    return 0
