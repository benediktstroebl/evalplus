def minSubArraySum(nums):
    m = 0
    for i in range(len(nums)):
        if nums[i] > m:
            m = nums[i]
    return m