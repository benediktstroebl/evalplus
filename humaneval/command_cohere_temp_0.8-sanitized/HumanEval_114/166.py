def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of the given array of integers nums.
    """
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    
    return min(min_sum, max_sum)
nums = [2, 3, 4, 1, 2, 4]