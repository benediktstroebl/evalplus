def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of nums.
    """
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    for num in nums[1:]:
        min_sum = min(num, min_sum + num)
        max_sum = max(num, max_sum + num)
    
    return min_sum if min_sum == max_sum else -max_sum