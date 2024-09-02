import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # get the sum of the array
    array_sum = sum(nums)

    # get the length of the array
    array_length = len(nums)

    # get the minimum sum of a subarray
    # this is the sum of the array itself
    # it is not the minimum
    min_sum = sum(nums)

    # get the total sum of all the elements in the subarray
    # initialize it to zero
    total_sum = 0

    # for each index in the array,
    # get the current sum of the subarray
    # if the current sum is greater than the minimum,
    # set the minimum to the current sum
    # move on to the next subarray
    for i in range(array_length):
        for j in range(i, array_length):
            total_sum += nums[j]
            if total_sum > min_sum:
                min_sum = total_sum
            # if the sum is greater than the array,
            # there is no point in continuing
            # break out of the inner loop
            if total_sum >= array_sum:
                break
        # reset the total sum to zero
        # at the end of each inner loop
        total_sum = 0
    return min_sum

