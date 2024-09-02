import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Approach 1
    # time complexity O(n^2)
    # space complexity O(1)
    # res = math.inf
    # for i in range(len(nums)):
    #     tmp = 0
    #     for j in range(i, len(nums)):
    #         tmp += nums[j]
    #         res = min(res, tmp)
    # return res
    
    # Approach 2
    # time complexity O(n)
    # space complexity O(1)
    # total = sum(nums)
    # res = total
    # tmp = 0
    # for i in range(len(nums)):
    #     tmp += nums[i]
    #     res = min(res, tmp-total+i+1)
    # return res

    # Approach 3
    # time complexity O(n)
    # space complexity O(n)
    # tmp = 0
    # res = math.inf
    # dp = [0 for _ in nums]
    # dp[0] = nums[0]
    # for i in range(1, len(nums)):
    #     dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
    # for i in range(len(nums)):
    #     res = min(res, dp[i])
    # return res
    
    # Approach 4
    # time complexity O(n)
    # space complexity O(1)
    # cur = nums[0]
    # res = cur
    # for i in range(1, len(nums)):
    #     cur = max(cur+nums[i], nums[i])
    #     res = min(res, cur)
    # return res
    
    # Approach 5
    # time complexity O(n)
    # space complexity O(1)
    # cur = nums[0]
    # res = cur
    # for i in range(1, len(nums)):
    #     cur = max(
