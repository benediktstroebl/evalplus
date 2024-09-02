import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Sort the array
    nums = sorted(nums)
    # Initialize a variable to store the minimum sum
    min_sum = math.inf
    # Loop through the sorted array
    for i in range(len(nums) - 1):
        # If the current sub-array is non-empty
        if nums[i] != 0:
            # Update the minimum sum
            min_sum = min(min_sum, i*nums[i] + (nums[i + 1] if nums[i + 1] != 0 else 0))
        else:
            # If the current sub-array is empty, update the minimum sum to the current element
            min_sum = min(min_sum, i*nums[i])
    return min_sum

test = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(test))
