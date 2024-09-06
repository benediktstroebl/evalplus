import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Getting the length of the array
    length = len(nums)

    # Initializing the min_sum variable to the maximum value
    min_sum = math.inf

    # Initializing the start and end indexes
    start = 0
    end = 0

    # Looping through the array
    while end < length:
        # Calculating the current sum of the sub array
        sub_sum = sum(nums[start:end + 1])

        # If the current sum is less than the min_sum
        # then we update the min_sum variable with the current sum
        if sub_sum <= min_sum:
            min_sum = sub_sum

        # If the sub array contains only one element
        # then we increment the start index
        if end - start == 0:
            start += 1

        # We increment the end index
        end += 1

    # Returning the min_sum
    return min_sum
