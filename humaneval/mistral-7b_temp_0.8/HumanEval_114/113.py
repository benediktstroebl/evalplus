import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # get sum of array elements
    totalSum = sum(nums)
    # set min subarray sum to total sum of the array
    minSubArraySum = totalSum
    # if the array has only one element
    if len(nums) == 1:
        return nums[0]
    # set currentSum and start to 0
    currentSum = start = 0
    # iterate through the array
    for i in range(len(nums)):
        # check if current sum is less than min subarray sum
        # if so, set min subarray sum to current sum
        if currentSum < minSubArraySum:
            minSubArraySum = currentSum
        # if the current sum is greater than total sum of array
        # minus the starting element, set the starting element to the current element
        if currentSum > totalSum - nums[start]:
            start = i
        # add the current element to current sum
        currentSum += nums[i]
    # return the min subarray sum
    return minSubArraySum

