import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sums = []
    for i in range(len(nums)):
        if i == len(nums) - 1:
            sums.append(nums[i])
        else:
            sums.append(nums[i])
            if sums[-1] > 0:
                min_sum = max(nums[-2:-1])
                sums.append(min_sum)
    return sums[-1]
