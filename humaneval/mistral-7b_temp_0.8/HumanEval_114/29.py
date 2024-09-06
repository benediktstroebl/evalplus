import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # If the array is empty, return
    if not nums:
        return None
    # Set the minimum sum of the first value in the array, since the first value is always in a subarray
    min_sum = nums[0]
    # Set the start and end indices of the minimum subarray to 0 and 1, respectively
    start = 0
    end = 1
    # Loop through the array, starting from the second value
    for i in range(1, len(nums)):
        # Set the temporary sum of the subarray to the sum of the start and end values
        temp_sum = nums[start] + nums[end]
        # If the temporary sum is less than the current minimum sum, update the minimum sum and start and end indices
        if temp_sum < min_sum:
            min_sum = temp_sum
            start = end - 1
            end = i
        # Update the end index to the next value in the array
        end += 1
    # Return the minimum sum
    return min_sum
