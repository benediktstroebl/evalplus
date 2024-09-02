import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # O(n^2) solution
    # for i in range(len(nums)):
    #     sum = 0
    #     for j in range(i, len(nums)):
    #         sum += nums[j]
    #         if sum < 0:
    #             sum = 0
    #     if sum < smallest:
    #         smallest = sum

    # return smallest

    # O(n) solution
    sum = 0
    smallest = float('inf')

    for i in range(len(nums)):
        sum += nums[i]

        if sum < 0:
            sum = 0
        elif sum < smallest:
            smallest = sum

    return smallest
