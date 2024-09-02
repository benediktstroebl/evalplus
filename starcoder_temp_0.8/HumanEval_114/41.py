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

    # we are looking for a contiguous subarray with the smallest sum
    # the sum of the subarray will be the total sum minus the minimum value in the subarray
    # the minimum value in the subarray will be the minimum sum of any subarray that ends on nums[i]
    # the minimum sum of any subarray that ends on nums[i] will be the minimum of either:
    # 1. the total sum minus the current minimum value in the subarray
    # 2. the total sum minus the current number at index i
    # the smallest sum of any subarray that ends on nums[i] will be the min of these two values

    current_min = nums[0]
    total = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < current_min:
            current_min = nums[i]
        total += nums[i]

        if nums[i] < current_min:
            current_min = nums[i]
        else:
            current_min = min(current_min, total - nums[i])

    return total - current_min
