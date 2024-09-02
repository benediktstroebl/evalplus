import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    def helper(nums, target):
        """
        Returns the sum of a subarray of nums that is of minimal sum and has the
        given target sum.
        """
        start = 0
        end = 0
        total = 0

        while start < len(nums) and end < len(nums):
            total += nums[end]
            while total >= target:
                total -= nums[start]
                start += 1
            end += 1

        return total

    # Time: O(n)
    # Space: O(n)
    # n = len(nums)
    #
    # if n == 0:
    #     return 0
    #
    # min_subarray_sum = math.inf
    #
    # for i in range(n):
    #     cur_min_subarray_sum = helper(nums[i:], sum(nums[:i + 1]))
    #     min_subarray_sum = min(min_subarray_sum, cur_min_subarray_sum)
    #
    # return min_subarray_sum
