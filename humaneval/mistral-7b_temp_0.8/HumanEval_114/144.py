import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # initialize answer
    ans = nums[0]
    # initialization of the variable to hold the current subarray sum
    subArray = 0

    # traverse through the list and find the minimum sum
    for num in nums:
        # update subArray to hold the current subarray sum
        subArray = subArray + num
        # check if current subArray sum is smaller than the current answer
        if subArray < ans:
            ans = subArray
        # check if subArray is less than zero
        if subArray < 0:
            subArray = 0

    return ans
