import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = sum(nums)
    minSubArray = len(nums)

    # If array is empty, no subarray, so return 0
    if not nums:
        return 0

    # Try each starting point of the subarray
    for i in range(len(nums)):
        # Find minimum of all subarrays starting at i
        curSubArray = 0
        curSubArraySum = nums[i]
        for j in range(i, len(nums)):
            curSubArray += 1
            curSubArraySum += nums[j]
            # Keep track of min subarray
            if curSubArraySum < minSum:
                minSum = curSubArraySum
                minSubArray = curSubArray

    return minSubArray
