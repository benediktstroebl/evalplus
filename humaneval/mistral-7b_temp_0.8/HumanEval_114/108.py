import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    smallest_subarray = None
    smallest_sum = math.inf

    for i in range(len(nums)):
        current_sum = nums[i]
        for j in range(i+1, len(nums)+1):
            current_sum += nums[j-1]
            if smallest_sum > current_sum:
                smallest_sum = current_sum
                smallest_subarray = [i, j-1]

    return [smallest_subarray[0]+1, smallest_subarray[1]-smallest_subarray[0]]
