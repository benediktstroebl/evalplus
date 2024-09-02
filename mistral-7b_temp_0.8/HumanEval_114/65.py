import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Given an array of integers nums, find the minimum sum of any non-empty sub-array of nums.
    # Could you do this in O(n) time complexity?

    # Time: O(n), space: O(1)
    # use two pointer
    # use 0 as default,
    # every time sum is smaller than 0, we could update sum with the minimum of the current sum and 0
    # as the left pointer moves, the right pointer will move at the same time
    # update minimum with the minimum of the current minimum and the sum
    # if the current sum is equal to 0, the minimum should be 0
    # when the right pointer is out of range, return the minimum
    # in this case, we don't need to use list.pop(0) as we are using two pointer

    # nums = [-1, -2, -3, -4, -5, -6]
    # nums = [2,3,4,1,2,4]
    # nums = [3,2,4,1,2,4]
