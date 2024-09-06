import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # A variant of the above algorithm is to use a similar algorithm to find
    # the largest sum in a subarray. The idea is to keep track of 4 sums:
    #
    # 1. The sum of the whole array (full_sum)
    # 2. The sum of the elements in the subarray so far (partial_sum)
    # 3. The minimum of the above two numbers (min_sum)
    # 4. The maximum of the above two numbers (max_sum)

    full_sum = sum(nums)
    partial_sum = min_sum = max_sum = 0
    for num in nums:
        partial_sum += num
        max_sum = max(max_sum, partial_sum)
        min_sum = min(min_sum, partial_sum)

    return min(full_sum - max_sum, min_sum)

