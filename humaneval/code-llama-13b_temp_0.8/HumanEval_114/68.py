import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # for empty lists, default answer is math.inf
    if not nums:
        return math.inf

    # initialize two variables, min_sum and total
    min_sum = math.inf
    total = 0

    # iterate through the list from left to right
    for i in range(len(nums)):
        # increment total by current element
        total += nums[i]
        # check if total is less than min_sum
        if total < min_sum:
            # set min_sum to new minimum
            min_sum = total
        # check if total is less than zero
        if total < 0:
            # reset total
            total = 0

    return min_sum

