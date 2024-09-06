import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Assuming nums[0] is smallest sum, start with that
    # array minimum sum is initialized at nums[0]
    min_sum = nums[0]
    # For each element of nums
    for i in range(1, len(nums)):
        # Compare element with minimum sum
        if nums[i] < min_sum:
            # If element is smaller than min_sum, update min_sum
            min_sum = nums[i]
        # If element is larger or equal to min_sum, check if element + min_sum is smaller than min_sum
        elif nums[i] + min_sum < min_sum:
            # If it is smaller, update min_sum
            min_sum = nums[i] + min_sum
        # Else do nothing
    return min_sum
