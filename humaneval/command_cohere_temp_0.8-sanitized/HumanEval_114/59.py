def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of nums.
    
    Args:
        nums (list): Array of integers
    
    Returns:
        int: Minimum sum of a non-empty sub-array
    """
    # Find the maximum and minimum values in the array
    max_val = max(nums)
    min_val = min(nums)
    
    # Calculate the potential sum at the extreme points
    max_potential = max_val * (len(nums) - 1)
    min_potential = min_val * (len(nums) - 1)
    
    # If all values in array are positive, return maxPotential
    if max_val >= min_val:
        return max_potential
    
    # If all values are negative, return minPotential
    elif min_val >= max_val:
        return min_potential
    
    # If mixed, return min of maxPotential and sum of nums[0..n-1]
    else:
        return min(max_potential, sum(nums))