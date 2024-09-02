import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # check if the array is empty
    if not nums:
        return -1

    # check if the array has only one number
    if len(nums) == 1:
        return nums[0]

    # sort the array in ascending order
    nums.sort()

    # initialize variables to keep track of the sub-array sum and the minimum sum found so far
    curr_sum = nums[0]
    curr_min_sum = nums[0]
    curr_index = 0

    # iterate through the array
    for i in range(1, len(nums)):
        # if the current sub-array sum is less than the current minimum sum
        if curr_sum <= curr_min_sum:
            # update the sub-array sum and the minimum sum
            curr_sum += nums[i]
            curr_min_sum = min(curr_min_sum, curr_sum)
        else:
            # update the sub-array sum and update the index to start the next sub-array
            curr_sum += nums[i]
            curr_index += 1
            curr_min_sum = min(curr_min_sum, curr_sum)

    # return the minimum sum of any non-empty sub-array
    return curr_min_sum
