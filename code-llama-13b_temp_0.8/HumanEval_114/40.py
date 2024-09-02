import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # we only need to go through every index (not index + 1)
    for i in range(len(nums)):

        sum = 0

        for j in range(i, len(nums)):
            # add the current index value to sum
            sum += nums[j]
            # check if current sum is less than minimum or not
            if sum < minimum:
                minimum = sum

    # return minimum
    return minimum
