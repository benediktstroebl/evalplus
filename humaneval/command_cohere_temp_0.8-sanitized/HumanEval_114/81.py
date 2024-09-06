def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = nums[0]
        if num < current_sum:
            current_sum = num
        min_sum = min(min_sum, current_sum)
        max_sum = max(max_sum, current_sum)
    
    return min(min_sum, max_sum)
nums = [2, 3, 4, 1, 2, 4]