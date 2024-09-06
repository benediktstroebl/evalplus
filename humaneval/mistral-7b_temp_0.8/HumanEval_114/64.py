import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    else:
        min_sum = 1000000000
        for i in range(n):
            num_sum = nums[i]
            for j in range(i, n):
                num_sum += nums[j]
                min_sum = min(min_sum, num_sum)

        return min_sum
