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
        return min(nums[0], nums[1])
    sums = []
    if nums[0] <= 0 and nums[1] <= 0:
        sums.append(nums[0] + nums[1])
    elif nums[0] > 0 and nums[1] <= 0:
        sums.append(nums[0])
    elif nums[0] <= 0 and nums[1] > 0:
        sums.append(nums[1])
    else:
        sums.append(nums[0] + nums[1])
    for i in range(2, len(nums)):
        if nums[i] + nums[i - 1] <= 0:
            sums.append(nums[i])
        else:
            sums.append(nums[i] + nums[i - 1])
    return min(sums)
