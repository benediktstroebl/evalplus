import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Check if any element in the array is 0
    if sum(nums) == 0:
        return -1
    
    # Traverse through the array and keep track of the minimum sum of each sub-array
    min_sum = math.inf
    left = 0
    right = 0

    for i in range(len(nums)):
        if left == right:
            # We have reached the end of the array and have not found a sub-array with a sum below the current minimum
            if right - left + 1 != 0:
                return -1
            # Reset the current sub-array to the first element
            right = i + 1
            left = i
        elif nums[left] <= nums[right]:
            # We have found a sub-array with a sum below the current minimum
            current_sum = right - left + 1
            if current_sum < min_sum:
                min_sum = current_sum
                left = right = i + 1
        else:
            # We have reached the end of the array and have not found a sub-array with a sum below the current minimum
            if right - left + 1 != 0:
                return -1
            # Reset the current sub-array to the first element
            right = i + 1
            left = i
    return min_sum
