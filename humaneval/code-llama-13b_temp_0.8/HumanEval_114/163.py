import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # create a variable to store the minimum sum of any subarray
    min_sum = nums[0]
    # create a variable to store the sum of the current subarray
    # initialize to 0
    sum = 0
    # loop over each element in nums
    for i in range(len(nums)):
        # add the value of the element to the sum
        sum += nums[i]
        # if the sum is less than the current min, update the min
        if sum < min_sum:
            min_sum = sum
        # check if the sum is less than 0
        # if so, reset the sum to 0
        if sum < 0:
            sum = 0
    # return the min subarray sum
    return min_sum

