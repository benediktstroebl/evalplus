import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # We are going to iterate over the array once.
    # We're going to create a min sum to track the minimum
    # we've seen so far, and a sum to track our current
    # sum

    # Base Case
    min_sum = float('inf')

    # This is a pointer to the current index
    # i = 0
    # sum = nums[0]
    # min_sum = nums[0]

    for i, num in enumerate(nums):
        print("i:", i)
        print("num:", num)
        # We can reduce the amount of memory we use by only
        # adding the current num to the sum, and then
        # updating the min_sum
        sum += num
        if min_sum > sum:
            min_sum = sum

    return min_sum

