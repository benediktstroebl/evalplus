import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Sum of the whole array
    arr_sum = sum(nums)

    # Minimum sum of sub-array is going to be the array's sum
    min_sum = arr_sum

    for i in range(len(nums)):
        # Initially we assume that the sum of the sub-array
        # starting from 0th index is going to be the minimum
        # sum of sub-array
        current_sum = 0

        # The sum of the sub-array is going to be equal to the sum of the
        # sub-array starting from the index (i) and ending at the last index
        # in this case (n-1).
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum < min_sum:
                min_sum = current_sum
            if current_sum > arr_sum:
                break

    return min_sum

