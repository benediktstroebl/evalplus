import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # ! so this problem is finding the min sum of a sub-array
    # ! so the sub-array MUST contain the first element, otherwise it isn't a sub-array
    # ! for the sub-array to be the minimum length possible, it must be the length of one
    # ! we also know that the sum of the sub-array can't be smaller than the value of that one element
    # ! so we know that the minimum sum possible is the value of that one element
    # * dynamic programming (DP) problem

    # * init a variable that will store the minimum sum
    minimum_sum = nums[0]

    # * loop over the subarrays and find the sum of each one
    # * if that sum is less than the minimum sum, update the minimum sum
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum < minimum_sum:
                minimum_sum = sum

    return minimum_sum

