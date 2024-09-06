import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Use a variable to store the min
    min = math.inf

    # Use a variable to store the cumulative sum
    total = 0

    # Iterate over each number
    for i in range(len(nums)):

        # Increment the total
        total += nums[i]

        # If the total is less than the min, set min to total
        if total < min:
            min = total

        # If the total is negative, reset the total to 0
        if total < 0:
            total = 0

    return min



