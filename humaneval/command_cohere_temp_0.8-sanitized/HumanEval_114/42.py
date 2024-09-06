def minSubArraySum(nums):
    curSum = 0
    minSum = numSanityCheck(nums)

    for num in nums:
        curSum += num
        minSum = min(minSum, curSum)
        curSum -= max(curSum // 3, num)

    return minSum
def numSanityCheck(nums):
    if all(num < 0 for num in nums) or all(num > 0 for num in nums):
        return min(num for num in nums if num != 0)
    return 0