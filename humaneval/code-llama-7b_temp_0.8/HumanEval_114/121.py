import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Initialization
    # minSubArraySum := the sum of the first subarray (of 1 element)
    minSubArraySum = nums[0]

    # remainingSubArraySum := sum of the remaining subarray after removing the first subarray (of 1 element)
    remainingSubArraySum = sum(nums[1:])

    # Update minSubArraySum
    if minSubArraySum > remainingSubArraySum:
        minSubArraySum = remainingSubArraySum

    # Update remainingSubArraySum
    remainingSubArraySum -= nums[0]

    # Loop
    for i in range(1, len(nums)-1):
        # Update minSubArraySum
        if minSubArraySum > remainingSubArraySum:
            minSubArraySum = remainingSubArraySum

        # Update remainingSubArraySum
        remainingSubArraySum -= nums[i]

    return minSubArraySum
