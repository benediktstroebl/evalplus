import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    mem = {}
    for i in range(len(nums)):
        mem[i] = nums[i]
        for j in range(i+1, len(nums)):
            mem[j] = mem[j]+nums[j]
    minim = math.inf
    for k in range(len(nums)):
        if(mem[k]<0):
            continue
        if(mem[k]<minim):
            minim = mem[k]
    return minim
