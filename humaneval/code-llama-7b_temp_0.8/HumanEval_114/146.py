import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Initialize minSum to a very large number.
    minSum = math.inf
    # We'll track the current subarray's sum as curSum.
    curSum = 0
    # The starting index of the current subarray.
    start = 0

    # For each index after the first in the array,
    for end in range(1, len(nums)):
        # Add the next element to our current subarray sum.
        curSum += nums[end]
        # Update minSum if needed.
        minSum = min(minSum, curSum - nums[start])

        # If we've now gotten a subarray sum > the current subarray sum,
        # remove the first element from our subarray.
        if curSum - nums[end] > curSum:
            start += 1
    return minSum
