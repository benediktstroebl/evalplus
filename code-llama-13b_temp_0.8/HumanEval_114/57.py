import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # set the current minimum to a value of infinity
    min_sum = math.inf
    # set the current sum to 0
    curr_sum = 0
    # iterate through the array
    for num in nums:
        # add the current number to the sum
        curr_sum += num
        # if the current sum is less than the minimum
        if curr_sum < min_sum:
            # set the minimum to the current sum
            min_sum = curr_sum
        # if the current sum is greater than 0
        if curr_sum > 0:
            # reset the current sum to 0
            curr_sum = 0
    # return the minimum sum
    return min_sum
