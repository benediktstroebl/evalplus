def minSubArraySum(nums):
    curSum = 0
    minSum = numRel = float('inf')
    
    for num in nums:
        curSum += num
        relSum = curSum - numRel
        minSum = min(minSum, relSum)
        numRel = min(numRel, curSum)
    
    return minSum