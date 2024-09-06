def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    result = nums[0]
    
    for n in nums[1:]:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum + n, n)
        result = min(result, max_sum)
    
    return result
nums = [2, 3, 4, 1, 2, 4]