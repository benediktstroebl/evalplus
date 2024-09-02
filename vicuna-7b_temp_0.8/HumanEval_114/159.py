import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Check for special case of empty input
    if not nums:
        return 0
    
    # Find the first negative number
    for i in range(len(nums)):
        if nums[i] < 0:
            start = i
            break
    
    # Check if we can find a valid sub-array
    for i in range(start, len(nums)):
        # Find the sub-array sum
        sum = nums[start] + nums[i]
        if sum < 0:
            continue
        else:
            # Find the minimum sub-array sum
            min_sum = sum
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum < min_sum:
                    min_sum = sum
            return min_sum
    # If no valid sub-array is found, return 0
    return 0
