import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # This is a brute force solution.
    #
    # Time complexity: O(n^2) - for each element in the input array, we iterate through
    # every other element to find the smallest sub array
    # Space complexity: O(1) - no additional data structures created

    min_sum = math.inf
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            min_sum = min(min_sum, sum(nums[i:j+1]))
    return min_sum

    # This is a dynamic programming solution.
    #
    # Time complexity: O(n) - one iteration through the input array
    # Space complexity: O(n) - an array of n elements is created and returned

    # min_sum = math.inf
    # min_sums = [math.inf] * len(nums)
    # min_sums[0] = nums[0]

    # for i in range(1, len(nums)):
    #     min_sums[i] = min(nums[i], min_sums[i-1]+nums[i])

    # return min(min_sums)
