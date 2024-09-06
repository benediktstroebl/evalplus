import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # (1) Find the sum of the whole array
    # (2) For each number in the array, find a subarray that has the number and add it to an array
    # (3) Return the min value in that array

    sumOfWholeArray = sum(nums)

    minSubArraySum = [sumOfWholeArray]

    for number in nums:
        subArraySum = number + sumOfWholeArray
        minSubArraySum.append(subArraySum)
        sumOfWholeArray -= number

    return min(minSubArraySum)
