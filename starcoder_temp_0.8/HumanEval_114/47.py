import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Dynamic Programming Approach
    # Time complexity: O(n)
    # Space complexity: O(1)
    # 1. Find the max subarray sum in nums
    # 2. Find the min subarray sum of nums from i to j

    # Find the max subarray sum in nums
    max_subarray_sum = nums[0]
    for i in range(1, len(nums)):
        max_subarray_sum = max(max_subarray_sum + nums[i], nums[i])

    # Find the min subarray sum from i to j
    min_subarray_sum = math.inf
    for j in range(len(nums)):
        min_subarray_sum = min(min_subarray_sum, max_subarray_sum - nums[j])

    return min_subarray_sum
