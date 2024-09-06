def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of nums.
    """
    if not nums:
        return 0
    
    min_so_far = nums[0]
    max_ending_here = nums[0]
    
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        min_so_far = min(min_so_far, max_ending_here)
    
    return min_so_far