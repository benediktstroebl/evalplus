import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = float("inf")
    # start, end and sum are the start and end indexes and sum of array elements
    # in the subarray
    start = 0
    end = 0
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        # if the sum is less than minSum, then update minSum
        if (sum < minSum):
            minSum = sum
            start = 0
            end = i
        # if the sum is greater than minSum, then we can shift start index
        # to find the min sum
        elif (sum >= minSum):
            while(sum >= minSum):
                sum -= nums[start]
                start += 1
            minSum = sum
            end = i
    return minSum
