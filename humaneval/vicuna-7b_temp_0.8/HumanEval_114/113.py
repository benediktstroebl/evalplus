import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    m = len(nums)
    sum_list = [0] * m
    for i in range(1, m):
        for j in range(i):
            if nums[j] < 0:
                for k in range(j, m):
                    sum_list[k] -= nums[k]
                    nums[k] = 0
                    break
            else:
                sum_list[i] += nums[j]
                for k in range(j+1, m):
                    sum_list[k] -= nums[k]
    return sum_list[1] if sum_list[1] != 0 else sum_list[0]
