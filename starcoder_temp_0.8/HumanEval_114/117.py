import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 暴力求解，O(n^2)
    # for i in range(0, len(nums)):
    #     result = 0
    #     for j in range(i, len(nums)):
    #         result += nums[j]
    #     if result < result_min:
    #         result_min = result
    # return result_min

    # 双指针求解，O(n)
    # 首先我们用前两个数求和，然后计算前两个数的和
    # 然后我们在循环的过程中，每次都和最小的结果进行比较
    # 如果当前的和小于最小的结果，就更新最小的结果
    # 但是，我们还得注意更新最小结果的时候，还需要移动左指针
    result_min = float("inf")
    sum_min = 0
    i, j = 0, 0
    while j < len(nums):
        sum_min += nums[j]
        j += 1
        while i < j and sum_min > result_min:
            sum_min -= nums[i]
            i += 1
        if sum_min < result_min:
            result_min = sum_min
    return result_min

