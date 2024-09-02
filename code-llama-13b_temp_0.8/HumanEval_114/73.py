import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    #A subarray of nums. 
    #If sum of the subarray is zero, return zero
    #If sum of subarray is greater than zero, return the sum of the subarray
    if sum(nums) > 0:
        return sum(nums)
    #For subarray of length 1. If the subarray is empty, return 0. If the subarray is not empty, return the number in the subarray
    if len(nums) == 1:
        return 0 if nums[0] == 0 else nums[0]

    #If the array is not zero, and the length is greater than 1:
    #Declare the minimum sum to be the maximum possible value for a python int
    minSum = math.inf
    #Declare the total sum to be 0
    total = 0
    #For each number in the array:
    for num in nums:
        #Add the number to the total sum
        total += num
        #If the total sum is greater than zero:
        if total > 0:
            #If the total sum is less than the minimum sum, set the minimum sum to the total sum
            if total < minSum:
                minSum = total
            #Set the total sum to zero
            total = 0

    #Return the minimum sum
    return minSum
