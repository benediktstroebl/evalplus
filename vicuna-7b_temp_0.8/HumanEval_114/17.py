import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Check if the array is empty
    if not nums:
        return -1
    
    # Initialize the sum of the sub-array to the first element of the array
    sum = nums[0]
    for num in nums[1:]:
        sum += num
    
    # Initialize the minimum sum of non-empty sub-array
    min_sum = float('inf')
    for i in range(len(nums)-1):
        # Initialize the current sub-array to the current element to the end of the array
        curr_sum = sum - nums[i+1]
        for j in range(i+1, len(nums)):
            # If the current sub-array is non-empty and the sum is less than the minimum sum
            if curr_sum + nums[j] <= min_sum and curr_sum != 0:
                # Update the sum of the current sub-array
                curr_sum += nums[j]
            else:
                # Update the minimum sum of non-empty sub-array
                min_sum = min(min_sum, curr_sum)
    
    return min_sum
