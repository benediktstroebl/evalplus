def minSubArraySum(nums):
    curSum = 0
    minSum = numSucc = float('inf')
    for num in nums:
        curSum += num
        succSum = curSum - minSum
        if succSum < numSucc:
            minSum = curSum
            numSucc = succSum
        elif succSum > numSucc:
            numSucc = succSum
        elif succSum == numSucc:
            minSum = min(minSum, curSum)
    return minSum