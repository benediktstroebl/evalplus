def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of nums.
    """
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    for num in nums[1:]:
        min_sum = min(min_sum + num, num)
        max_sum = max(max_sum + num, num)
    
    return min(min_sum, max_sum)
nums = [2, 3, 4, 1, 2, 4]