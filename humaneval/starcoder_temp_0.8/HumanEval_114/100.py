import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # this is a dynamic programming question
    # the idea is that we need to find the minimum number of subarray sum
    # we start with a sum of 0, we check all possible subarrays and find the
    # one that gives the minimum sum of subarrays, then we try to use a sliding
    # window to find a smaller number of subarrays
    # note that there could be multiple subarrays of the same length that give
    # the same sum, so we need to keep a variable to record the minimum sum of
    # subarrays
    # the next problem is how to deal with the edge cases
    # if we have a subarray that sums to the same value as the original array,
    # then the min sum should be the sum of the array, so we will use an if
    # statement to check for that edge case
    # we will also add a few checks to make sure we're not entering an infinite
    # loop
    # then, we will create a for loop to find all the subarrays with the minimum
    # sum
    # if a new subarray's sum is less than the minimum, then we will update the
    # minimum
    # if a new subarray's sum is greater than the minimum, then we will do
    # nothing because we already have the minimum
    if len(nums) == 1:
        return nums[0]
    else:
        # we will start the sum at 0
        min_sum = 0
        # the first sum we will check will be the first number in the array
        # so we start a for loop at 1
        for i in range(1, len(nums)):
            # the for loop will continue until the end of the array
            # we will check every subarray
            # we need a variable to keep track of the current sum
            curr_sum = 0
            # we need a variable to keep track of the number of elements
            # in the subarray
            num_elements = 0
            # we will start a j value at i
            for j in range(i, len(nums)):
                # we will add each number to the current sum
                # we will increment the number of elements in the subarray
                # and update the current sum
                curr_sum = curr_sum + nums[j]
                num_elements = num_elements + 1
                # if the current sum is less than the minimum sum, then we will
                # update the minimum sum
