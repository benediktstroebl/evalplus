import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    def minSubArraySum_recursive(nums, left, right):
        if left >= right:
            return nums[left]
        mid = (left + right) // 2
        left_sum = minSubArraySum_recursive(nums, left, mid)
        right_sum = minSubArraySum_recursive(nums, mid + 1, right)
        # min sum so far
        min_sum = min(left_sum, right_sum)
        # sum of the current range
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += nums[i]
            min_sum = min(min_sum, curr_sum)
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            min_sum = min(min_sum, curr_sum)
        return min_sum

    def minSubArraySum_iterative(nums, left, right):
        if left >= right:
            return nums[left]
        mid = (left + right) // 2
        left_sum = minSubArraySum_iterative(nums, left, mid)
        right_sum = minSubArraySum_iterative(nums, mid + 1, right)
        # min sum so far
        min_sum = min(left_sum, right_sum)
        # sum of the current range
        curr_sum = 0
        min_left, min_right = mid, mid + 1
        for i in range(mid, left - 1, -1):
            curr_sum += nums[i]
            if curr_sum < min_sum:
                min_sum = curr_sum
                min_left = i
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            if curr_sum < min_sum:
                min_sum = curr_sum
                min_right = i
        return min_sum

    return minSubArraySum_recursive(nums, 0, len
