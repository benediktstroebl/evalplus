import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # if the array is empty, return 0
    if nums == []:
        return 0

    # intialize variables to track min, max, and sum
    curr_min = nums[0]
    curr_max = nums[0]
    curr_sum = nums[0]

    # loop through the array from the second element
    for i in range(1, len(nums)):
        # update the min/max/sum
        if nums[i] < curr_min:
            curr_min = nums[i]
        if nums[i] > curr_max:
            curr_max = nums[i]
        curr_sum += nums[i]

        # if the sum is less than the min, update min
        if curr_sum < curr_min:
            curr_sum = curr_min

    return curr_sum
