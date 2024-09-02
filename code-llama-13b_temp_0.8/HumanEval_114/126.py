import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # first try: O(n^2)
    # def sumArray(subarray):
    #     return sum(subarray)

    # min_sum = nums[0]
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         if min_sum > sumArray(nums[i:j+1]):
    #             min_sum = sumArray(nums[i:j+1])

    # return min_sum

    # print(minSubArraySum([-1, -2, -3]))
    # print(minSubArraySum([2, 3, 4, 1, 2, 4]))

    # second try: O(n)
    # def sumArray(subarray):
    #     return sum(subarray)

    # min_sum = nums[0]
    # min_sum_tmp = nums[0]
    # for i in range(1, len(nums)):
    #     min_sum_tmp = min(min_sum_tmp + nums[i], nums[i])
    #     if min_sum > min_sum_tmp:
    #         min_sum = min_sum_tmp

    # return min_sum

    # third try: O(1)
    min_sum = math.inf
    min_sum_tmp = 0
    for i in range(len(nums)):
        min_sum_tmp = max(min_sum_tmp + nums[i], nums[i])
        if min_sum > min_sum_tmp:
            min_sum = min_sum_tmp

    return min_sum

    # print(minSubArraySum([-1, -2, -3]))
    # print(minSubArraySum([2, 3, 4, 1, 2, 4]))
