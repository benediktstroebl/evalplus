def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return max(max_sum, min_sum)