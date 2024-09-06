import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    #create a new variable, total, and set to equal the first number in the array
    total = nums[0]
    #create a new variable, minSum, and set to equal the first number in the array
    minSum = nums[0]

    #for loop that iterates through the array
    for i in range(1, len(nums)):
        #if the sum of two numbers is smaller than the total, set total to the sum of the two numbers
        if (total + nums[i]) < total:
            total = total + nums[i]
        #if the sum of two numbers is larger than the total, set the total to the sum of the two numbers
        if (total + nums[i]) >= total:
            total = total + nums[i]
        #if the sum of two numbers is smaller than the minSum, set minSum to the sum of the two numbers
        if (total + nums[i]) < minSum:
            minSum = total + nums[i]
        #if the sum of two numbers is larger than the minSum, set minSum to the sum of the two numbers
        if (total + nums[i]) >= minSum:
            minSum = total + nums[i]
    return minSum

