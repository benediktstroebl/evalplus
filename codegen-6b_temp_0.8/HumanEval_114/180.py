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
    for i in range(len(nums) + 1):
        tmp = 0
        for j in range(i, len(nums) + 1):
            tmp += nums[j - 1]
            if tmp == 0:
                return 0
            elif tmp not in sums:
                sums.append(tmp)
    return min(sums)
