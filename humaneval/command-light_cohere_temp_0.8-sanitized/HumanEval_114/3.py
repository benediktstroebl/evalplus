def minSubArraySum(nums):
    if not_nums or not nums:
        return 0
    
    max_sum = current_sum = -1000000009
    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
    return max_sum