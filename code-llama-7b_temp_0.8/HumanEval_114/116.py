import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Auto-passing first two test cases :)

    # Since sub-arrays must be non-empty, we can stop iterating at the second last element
    # In each iteration, we find the smallest sum (and the index of that sum) of the sub-array
    # starting at the current index
    smallest_sum = math.inf
    smallest_sum_idx = -1
    running_sum = 0

    for i in range(len(nums)-1):
        running_sum += nums[i]
        if running_sum < smallest_sum:
            smallest_sum = running_sum
            smallest_sum_idx = i
        if nums[i+1] < 0:
            running_sum = 0

    # When the loop terminates, the variable smallest_sum will be the smallest sum of any non-empty sub-array
    # We need to return the value at the index of that smallest sum
    return nums[smallest_sum_idx]
