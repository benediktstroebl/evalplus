import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    # naive way
    # min_sum = float('inf')
    # for i in range(0,len(nums)):
    #     for j in range(i,len(nums)):
    #         temp = 0
    #         for k in range(i,j+1):
    #             temp += nums[k]
    #         min_sum = min(min_sum,temp)
    # return min_sum
    # time complexity: O(n^2)
    # space complexity: O(1)
    # better solution
    # time complexity: O(n)
    # space complexity: O(1)
    min_sum = float('inf')
    current_sum = 0
    for i in range(0,len(nums)):
        current_sum += nums[i]
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    if current_sum <
