def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum + n, n)
    return min(min_sum, max_sum)