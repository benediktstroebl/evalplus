import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def check(n, start, end):
        if start == end:
            return n
        mid = math.floor((start + end) / 2)
        left = check(n, start, mid)
        right = check(n, mid + 1, end)
        if left < right:
            return left
        return right

    def find_min(n, start):
        min_sum = math.inf
        current_sum = 0
        for i in range(start, len(n)):
            current_sum += n[i]
            if current_sum < min_sum:
                min_sum = current_sum
        return min_sum

    n = len(nums)
    if n < 2:
        return nums[0]
    return check(nums, 0, n - 1)
