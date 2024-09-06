def minSubArraySum(nums):
    curSum = 0
    minSum = numTimeout = float('inf')
    for num in nums:
        curSum += num
        if curSum < minSum:
            minSum = curSum
        if curSum > 0:
            numTimeout = max(numTimeout, curSum)
        else:
            numTimeout = max(numTimeout, curSum - 1)
    return minSum + numTimeout