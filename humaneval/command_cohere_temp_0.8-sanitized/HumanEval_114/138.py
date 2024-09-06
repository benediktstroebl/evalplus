def minSubArraySum(nums):
    curSum = 0
    minSum = numRel = float('inf')
    for num in nums:
        curSum += num
        mini = curSum - numRel
        numRel = min(numRel, curSum)
        minSum = min(minSum, mini)
    return minSum