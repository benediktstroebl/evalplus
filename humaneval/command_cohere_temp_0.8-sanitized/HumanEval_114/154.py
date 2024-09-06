def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    
    for num in nums[1:]:
        min_sum = min(num, min_sum + num)
        max_sum = max(max_sum, num)
    
    return min_sum + max_sum if max_sum else min_sum