import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    #initialise sum to the biggest number
    total = math.inf
    #initialise minimum sum to the smallest number
    min_total = -math.inf
    #set the number of elements to zero
    elements = 0
    for num in nums:
        #check if the total is bigger than the number
        if total > num:
            total = num
        #check if the min_total is smaller than the number
        if min_total < num:
            min_total = num
        #add one to the number of elements
        elements += 1
        #check if the min_total is bigger than the total
        if min_total > total:
            min_total = total

    return min_total

