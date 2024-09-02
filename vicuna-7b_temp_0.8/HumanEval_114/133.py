import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Check for empty array
    if not nums:
        return -float('inf')
    
    # Find the maximum and minimum number in the array
    max_num = max(nums)
    min_num = min(nums)
    
    # Create a dictionary to store the sub-array sums
    sub_array_sums = defaultdict(int)
    
    # Loop through the array
    for num in nums:
        # Increment the current sub-array sum
        sub_array_sums[num] += 1
        
        # If the current sub-array is not empty, update its sum
        if num != 0:
            sub_array_sums[max_num - num] -= 1
        
            # Update the maximum and minimum numbers
            max_num = max(nums)
            min_num = min(nums)
    
    # Find the minimum sub-array sum
    return min(sub_array_sums)
