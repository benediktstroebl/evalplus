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
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[0] + nums[1]

    # nums[0] + nums[1] + nums[2]
    # nums[0] + nums[1] + nums[2] + nums[3]
    # nums[0] + nums[1] + nums[2] + nums[3] + nums[4]
    # nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5]
    # nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6]
    # nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7]
    # nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7] + nums[8]
    # nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7] + nums[8] + nums[9]
    # nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7] + nums[8] + nums[9] + nums[10]
    # nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7] + num
