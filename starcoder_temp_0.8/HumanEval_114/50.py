import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum=0
    i=0
    j=0
    min=0
    max=math.inf
    while i<len(nums) and j<len(nums):
        sum+=nums[j]
        while sum>max:
            sum-=nums[i]
            i+=1
        if sum<min:
            min=sum
        j+=1
    return min
