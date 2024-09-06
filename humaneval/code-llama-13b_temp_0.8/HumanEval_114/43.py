import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 1st approach, brute force
    # check every subarray
    # O(n^2) time and space complexity
    """
    min_sum = math.inf
    for i in range(len(nums)):
        sub_arr = nums[i:]
        min_sum = min(min_sum, minSubArraySumHelper(sub_arr))
    return min_sum
    """
    # 2nd approach, Kadane's algorithm
    # O(n) time complexity
    min_sum = math.inf
    for i in range(len(nums)):
        sub_arr_sum = 0
        for j in range(i, len(nums)):
            sub_arr_sum += nums[j]
            min_sum = min(min_sum, sub_arr_sum)
    return min_sum
