import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_sum = None
    max_sum_index = None
    curr_sum = 0

    for i, val in enumerate(nums):
        if max_sum is None:
            max_sum = val
            max_sum_index = i
        else:
            curr_sum += val
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_sum_index = i
        print("max_sum:", max_sum, "curr_sum:", curr_sum)

    print("max_sum_index:", max_sum_index)
    if max_sum_index is not None:
        return nums[max_sum_index - 1]
    else:
        return 0

