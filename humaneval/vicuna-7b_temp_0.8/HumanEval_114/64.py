import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float('inf')
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0
        for j in range(i):
            if nums[j] >= 0:
                sub_array = [nums[i], nums[j+1]]
                sum = sub_array[0] + sub_array[1]
                if sum < min_sum:
                    min_sum = sum
                else:
                    min_sum -= sum
    return min_sum

nums = [1, -2, -3, 4, 1, -1, 2, 4, 2]
