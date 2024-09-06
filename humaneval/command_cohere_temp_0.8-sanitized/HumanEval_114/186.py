def minSubArraySum(nums):
    min_sum = float('inf')
    nums.sort(reverse=True)
    for i in range(1, len(nums)):
        min_sum = min(min_sum, nums[i] + nums[i-1])
    return min_sum