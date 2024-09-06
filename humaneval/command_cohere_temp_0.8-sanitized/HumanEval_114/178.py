def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    
    for x in nums:
        cur_sum += x
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    
    return min_sum
nums = [2, 3, 4, 1, 2, 4]