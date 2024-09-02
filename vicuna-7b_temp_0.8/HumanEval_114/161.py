import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    else:
        n = len(nums)
        for i in range(1, n):
            for j in range(i):
                if nums[j] < 0:
                    return -1
                elif nums[j] < nums[i]:
                    return -1
                elif nums[j] == nums[i]:
                    return -1
                else:
                    s = nums[i] - nums[j]
                    if s < nums[i]:
                        return -1
                    return s
