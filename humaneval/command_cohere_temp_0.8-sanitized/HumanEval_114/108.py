def minSubArraySum(nums):
    curSum = 0
    minSum = numArgs[0]
    
    for arg in nums:
        curSum += arg
        minSum = min(minSum, curSum)
        if curSum < 0:
            curSum = 0
    return minSum
nums = [2, 3, 4, 1, 2, 4]