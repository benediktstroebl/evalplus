def minSubArraySum(nums):
    curSum = 0
    minSum = numSol = float('inf')
    for num in nums:
        curSum += num
        if curSum < minSum:
            minSum = curSum
        if curSum > 0:
            numSol = min(numSol, curSum)
        if curSum < 0:
            numSol = min(numSol, -curSum)
    return minSum if minSum < numSol else numSol