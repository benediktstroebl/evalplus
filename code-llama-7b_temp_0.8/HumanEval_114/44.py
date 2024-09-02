import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Time complexity O(n)
    # Space complexity O(1)
    min_sub_array_sum = math.inf
    min_sum = math.inf
    current_sum = 0

    for num in nums:
        # update min_sum
        min_sum = min(min_sum, num)

        # update current_sum
        current_sum += num

        # update min_sub_array_sum
        min_sub_array_sum = min(current_sum - min_sum, min_sub_array_sum)

    return min_sub_array_sum
