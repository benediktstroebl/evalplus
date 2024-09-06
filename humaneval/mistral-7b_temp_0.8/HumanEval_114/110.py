import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Write your code here
    length = len(nums)
    min_sum = float('inf')
    min_range = (0, 0)

    for i in range(length):
        for j in range(i, length):
            sum = 0
            for k in range(i, j + 1):
                sum += nums[k]
            if sum < min_sum:
                min_sum = sum
                min_range = (i, j)

    return nums[min_range[0]:min_range[1] + 1]


