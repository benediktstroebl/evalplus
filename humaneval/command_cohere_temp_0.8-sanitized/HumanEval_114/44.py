def minSubArraySum(nums, k):
    """
    Finds the minimum sum of any sub-array within the 'nums' array.
    Args:
    - nums: Array of integers.
    - k: Offset added to minimum sub-array sum.
    
    Returns:
    - Minimum sum of a sub-array including the offset.
    """
    min_sum = float('inf')
    local_min = 0
    for i in range(len(nums)):
        local_min = nums[i] + local_min
        min_sum = min(min_sum, local_min)
    return min_sum - k