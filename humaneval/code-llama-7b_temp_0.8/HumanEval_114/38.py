import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    """
    def min_sub_array_sum(nums, min_sum, min_length, start, end):
        # Base case
        if start >= end:
            return min_sum, min_length

        # Recursive case
        min_sum_inc_start = min_sum
        min_length_inc_start = min_length
        min_sum_inc_end = min_sum
        min_length_inc_end = min_length

        if min_sum_inc_start > min_sum_inc_end:
            return min_sub_array_sum(nums, min_sum_inc_start, min_length_inc_start, start, start + 1)
        elif min_sum_inc_start < min_sum_inc_end:
            return min_sub_array_sum(nums, min_sum_inc_end, min_length_inc_end, end - 1, end)
        else:
            return min_sub_array_sum(nums, min_sum_inc_start, min_length_inc_start, start, end)
    """

    if not nums:
        return 0

    subarray_sum = 0
    min_sum = math.inf
    start = 0
    end = 0
    for index, num in enumerate(nums):
        subarray_sum += num
        if subarray_sum < min_sum:
            min_sum = subarray_sum
            start = 0
            end = index
        if subarray_sum > 0:
            subarray_sum = 0

    return min_sum

