import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # sort the input list
    nums = sorted(nums)

    # initialize the minimum sum to infinity
    min_sum = float('inf')

    # initialize the current sum to 0
    curr_sum = 0

    # initialize the current length to 1
    curr_len = 1

    # iterate through the input list
    for i in range(len(nums) - 1):
        # check if the current length is greater than 1
        if curr_len > 1:
            # update the current sum and length
            curr_sum += nums[i]
            curr_len -= 1
        else:
            # if the current length is 1, update the sum and add the next number
            curr_sum += nums[i]

        # update the minimum sum and the current sum
        min_sum = min(min_sum, curr_sum)
        curr_sum = 0

    # update the current sum and length
    curr_sum += nums[i]
    curr_len += 1

    # update the minimum sum
    min_sum = min(min_sum, curr_sum)

    return min_sum