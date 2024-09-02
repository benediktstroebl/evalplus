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
    elif len(nums) == 2:
        return min(nums[0], nums[1])
    else:
        temp = nums[0]
        best_sum = temp
        for i in range(1, len(nums)):
            if temp < 0:
                temp = nums[i]
            else:
                temp = nums[i] + temp
            if temp < best_sum:
                best_sum = temp
        return best_sum

