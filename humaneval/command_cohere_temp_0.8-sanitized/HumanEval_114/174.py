def minSubArraySum(nums):
    curSum = 0
    minSum = numSum = float('inf')
    
    for num in nums:
        curSum += num
        minSum = min(minSum, curSum)
        numSum = min(numSum, curSum)
    
    return min(minSum, numSum)