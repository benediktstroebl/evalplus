import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # TC O(N), SC O(1)
    def findMinSum(left, right, sum):
        if left > right:
            return math.inf
        elif left == right:
            return sum

        mid = (left + right) // 2
        l = findMinSum(left, mid - 1, sum + nums[mid])
        r = findMinSum(mid + 1, right, sum + nums[mid + 1])
        return min(l, r)

    return findMinSum(0, len(nums) - 1, 0)
