import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # init variables
    # sum of subarray
    subarray_sum = 0
    # start index
    start_idx = 0
    # minimum sum
    min_sum = math.inf
    # for each number in the array
    for i, num in enumerate(nums):
        # update sum of subarray
        subarray_sum += num
        # update minimum sum if needed
        min_sum = min(min_sum, subarray_sum - nums[start_idx])
        # update start_idx if necessary
        if subarray_sum < 0:
            start_idx = i + 1
    return min_sum
