def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        min_sum = min(min_sum, n)
        max_sum = max(max_sum, n)
    return min(min_sum, -max_sum)