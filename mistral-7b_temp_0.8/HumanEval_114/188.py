import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Iterate over the array with two pointers, one starting at 0, the other
    # incrementing by 1 for every iteration. Keep a running sum variable and
    # subtract the sum of the first element of the array from it on each iteration
    # as the first element will not be part of the subarray. Keep track of the
    # minimum sum as well.
    # If the sum of the subarray is greater than the minimum sum, then
    # the current subarray is not the minimum subarray. Else, update the minimum
    # sum variable to the current sum.
    # In the worst case, we need to compare the sums of all possible
    # subarrays, which is O(n^2), so we can say the runtime complexity is O(n^2)
    # In the worst case, we need to store all possible sums of subarrays, so we
    # can say the space complexity is O(n^2)
    min_sum = nums[0]
    running_sum = 0
    for i in range(len(nums)):
        for j in range(
