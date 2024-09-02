import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    #intialize variables
    smallest_sum=float("inf")
    current_sum=0
    #loop through the list
    for num in nums:
        #check if the sum is smaller than the current sum
        if current_sum+num<smallest_sum:
            #if so, update smallest_sum
            smallest_sum=current_sum+num
        #if not, add the number to current_sum
        current_sum+=num
    #return the smallest sum
    return smallest_sum


