import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    #first solution: dp, O(n^2) time complexity
    # https://discuss.leetcode.com/topic/11150/java-possible-solution-only-dp-computation-time-O(n-2-n)
    # minSum = float('inf')
    # for i in range(0,len(nums)):
    #     for j in range(i,len(nums)):
    #         minSum = min(minSum, sum(nums[i:j+1]))
    # return minSum
    #second solution: dp, O(n^2) time complexity
    #https://discuss.leetcode.com/topic/2796/java-solution-O(n)-time-O(1)
    # minSum = float('inf')
    # for i in range(0,len(nums)):
    #     minSum = min(minSum, sum(nums[i:]))
    # return minSum
    #third solution: best O(n)
    if not nums:
        return 0
    minSum, currentSum = nums[0], nums[0]
    for i in range(1, len(nums)):
        currentSum = max(nums[i], currentSum + nums[i])
        minSum = min(minSum, currentSum)
    return minSum
    # fourth solution: best O(nlogn)
    # if not nums:
    #     return 0
    # minSum = nums[0]
    # for i in range(1,len(nums)):
    #     nums[i] = max(nums[i], nums[i-1]+nums[i])
    #     minSum = min(minSum, nums[i])
    # return minSum

