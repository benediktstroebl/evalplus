import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # create a list to hold the sums of each subarray
    sums = []

    # loop through the array, holding the sum of the current subarray
    for i in range(len(nums)):

        # default the sum to 0
        currentSum = 0

        # loop through the remaining subarray
        for j in range(i, len(nums)):

            # add the current number to the sum
            currentSum += nums[j]

            # add the sum to the sums list
            sums.append(currentSum)

    # return the minimum subarray sum from the sums list
    return min(sums)
