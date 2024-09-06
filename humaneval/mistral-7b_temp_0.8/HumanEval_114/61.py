import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # find the minimum sum of any non-empty sub-array of nums
    minimum_sum = float('inf')
    # note this is subarray, so only need to compare prefix sum
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums) + 1):
    #         sub_arr = sum(nums[i:j])
    #         if sub_arr < minimum_sum:
    #             minimum_sum = sub_arr
    # return minimum_sum

    # the prefix sum is [0, 2, 4, 7, 10, 15]
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)

    # O(n)
    minimum_sum = prefix_sum[0]
    for i in range(1, len(prefix_sum)):
        if prefix_sum[i] - prefix_sum[i - 1] < minimum_sum:
            minimum_sum = prefix_
