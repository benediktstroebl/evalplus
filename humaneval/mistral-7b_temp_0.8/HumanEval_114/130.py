import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # if there is no subarray, return 0
    if len(nums) == 0:
        return 0
    # create a variable to store the minimum sum
    min_sum = math.inf
    # keep track of the minimum sum and the subarray index
    start_index = -1
    end_index = -1
    for i in range(len(nums)):
        # create a variable to keep track of the sum of the subarray
        sub_array_sum = 0
        # keep track of the start index of the subarray
        start = i
        # keep track of the end index of the subarray
        end = i
        # keep track of the current minimum sum
        current_min_sum = math.inf
        # keep track of the current minimum sum index
        current_min_index = -1
        # keep track of the current subarray sum
        current_subarray_sum = 0
        # keep track of the current start index
        current_start_index = -1
        # keep track of the current end index
        current_end_index = -
