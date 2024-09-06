def minSubArraySum(nums):
    curSum = 0
    minSum = numList[0]
    for num in nums:
        curSum += num
        minSum = min(minSum, curSum)
        if curSum < 0:
            curSum = 0
    return minSum
nums = [2, 3, 4, 1, 2, 4]