def minSubArraySum(nums):
    curSum = 0
    minSum = numArgs[0]
    
    for n in nums:
        curSum += n
        if curSum < 0:
            curSum = 0
        minSum = min(minSum, curSum)
    
    return minSum