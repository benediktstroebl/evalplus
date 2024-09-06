import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Keep track of the sum of the current subarray and the starting index of the current subarray
    # nums[curr - 1] == nums[j] + min_sum[j + 1]
    # min_sum[i] == min(nums[i], min_sum[i])
    min_sum = [0] * (len(nums) + 1)
    for i in range(1, len(nums)+1):
        min_sum[i] = nums[i-1] + min_sum[i-1]
    # Find the first starting index that sums to >= 0
    for i in range(len(nums) + 1):
        if min_sum[i] >= 0:
            break

    # Find the last ending index that sums to >= 0
    for i in range(len(nums) - 1, -1, -1):
        if min_sum[i] >= 0:
            break

    # For each index between i and j, figure out the min subarray sum and replace the corresponding
    # min_sum with the new value
    sums = min_sum[i:j+1]
    return min(sums)

