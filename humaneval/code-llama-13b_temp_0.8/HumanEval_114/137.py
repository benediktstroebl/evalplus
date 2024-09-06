import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # TODO: can we do better than O(n^2) ?

    def _minSubArraySum(nums, start, end):
        if start >= end:
            return math.inf

        mid = (start + end) // 2

        left_sum = _minSubArraySum(nums, start, mid)
        right_sum = _minSubArraySum(nums, mid + 1, end)
        mid_sum = min(nums[mid] + _minSubArraySum(nums, start, mid - 1), nums[mid] + _minSubArraySum(nums, mid + 1, end))

        return min(left_sum, right_sum, mid_sum)

    return _minSubArraySum(nums, 0, len(nums) - 1)
