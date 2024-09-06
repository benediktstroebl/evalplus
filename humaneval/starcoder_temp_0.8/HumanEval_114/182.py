import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Method 1
    # time: O(n^3), space: O(1)
    # for n, calculate the sum for sub-array of size n: O(n)
    # sum up the min value from all the sub-arrays: O(n^2)
    # for n sub-arrays, we take the min sum from all of them: O(n)
    # total time: O(n^3)

    # Method 2
    # time: O(n), space: O(1)
    # a sum is found from the beginning of the list
    # the sum of the list is calculated for each possible length
    # if the sum is less than the min sum found, then the min sum is updated
    # for n elements, the list is iterated n times, so the overall time complexity is O(n)

    # Method 3
    # time: O(n), space: O(1)
    # for n elements, the list is iterated once
    # the sum is updated from the beginning for each element in the list
    # the min sum is updated after each element is iterated
    # total time: O(n)

    # Method 4
    # time: O(n), space: O(1)
    # the sum of the list is calculated for each possible length
    # the min sum is updated when the sum is less than the min sum found
    # for n elements, the list is iterated n times, so the overall time complexity is O(n)

    # Method 5
    # time: O(n), space: O(1)
    # a sum is found from the end of the list
    # the sum of the list is calculated for each possible length
    # if the sum is less than the min sum found, then the min sum is updated
    # for n elements, the list is iterated n times, so the overall time complexity is O(n)

    # Method 6
    # time: O(n), space: O(1)
    # a sum is found from the beginning of the list
    # the sum of the list is calculated for each possible length
    # if the sum is less than the min sum found, then the min sum is updated
    # for n elements, the list is iterated n times, so the overall time complexity is O(n)

    # Method 7
    # time: O(n), space: O
