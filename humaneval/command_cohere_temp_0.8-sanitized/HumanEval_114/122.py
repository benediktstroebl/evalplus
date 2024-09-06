def minSubArraySum(nums):
    curSum = 0
    minSum = numList[0]
    for num in nums:
        curSum += num
        if curSum > 0:
            minSum = min(minSum, curSum)
        else:
            minSum = min(minSum, curSum + numList[0])
    return minSum
nums = [2, 3, 4, 1, 2, 4]