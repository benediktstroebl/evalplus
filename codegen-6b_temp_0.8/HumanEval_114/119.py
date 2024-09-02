import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    n = len(nums)
    minSubArray = nums[0]
    start = 0
    end = 0
    for i in range(1, n):
        if i == 1:
            minSubArray = nums[i]
        elif minSubArray + nums[i] < nums[i]:
            minSubArray = nums[i]
        else:
            minSubArray += nums[i]
        if minSubArray < 0:
            minSubArray = 0
        #print("i:", i, "minSubArray:", minSubArray, "end:", end)
        if i == n - 1:
            if minSubArray < 0:
                minSubArray = 0
            return minSubArray
        if i > end:
            start = i
            end = i + 1
            if end > n - 1:
                end = n - 1
            if minSubArray < 0:
                minSubArray = 0
            if minSubArray < minSubArray:
                minSubArray = minSubArray
            continue
        if minSubArray < minSubArray:
            minSubArray = minSubArray
        if minSubArray > 0:
            if minSubArray < minSubArray:
                minSubArray = minSubArray
    return minSubArray
