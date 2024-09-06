import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # init the sum to be -inf, so that if the sum is actually 0, the result will be 0
    # rather than a very small negative number
    min_sum = -float("inf")
    # keep track of the sum of the current subarray
    current_sum = 0
    # loop through the list, take the current element and add it to the current_sum
    # if the current_sum is less than 0, reset it to 0
    for num in nums:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        # if the current_sum is less than min_sum, replace it with the current_sum
        if current_sum < min_sum:
            min_sum = current_sum

    return min_sum
