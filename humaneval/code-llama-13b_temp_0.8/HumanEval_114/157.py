import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_sum = float('inf')
    running_sum = 0

    # Iterate over the array
    for index in range(len(nums)):
        # If the current value is less than the current running sum,
        #   then start a new running sum
        if (nums[index] < 0) and (running_sum + nums[index] < 0):
            running_sum = 0
        running_sum += nums[index]
        # If the current running sum is less than min_sum,
        #   then set min_sum to the running sum
        if running_sum < min_sum:
            min_sum = running_sum

    return min_sum
