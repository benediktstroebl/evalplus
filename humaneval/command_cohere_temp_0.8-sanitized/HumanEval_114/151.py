def minSubArraySum(nums):
    curSum = 0
    minSum = numUtil.MIN_VAL
    for n in nums:
        curSum += n
        if curSum < minSum:
            minSum = curSum
        elif curSum > 0:
            curSum -= nums[0]
        else:
            curSum = 0
    return minSum