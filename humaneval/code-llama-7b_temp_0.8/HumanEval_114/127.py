import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    #
    # O(n) time | O(1) space
    #
    if not nums:
        return None

    left, right = 0, 0

    min_sum = math.inf

    sum_so_far = 0
    while right < len(nums):
        sum_so_far += nums[right]
        min_sum = min(sum_so_far, min_sum)
        right += 1

    sum_so_far = 0
    while left < len(nums):
        sum_so_far += nums[left]
        min_sum = min(sum_so_far, min_sum)
        left += 1

    return min_sum
