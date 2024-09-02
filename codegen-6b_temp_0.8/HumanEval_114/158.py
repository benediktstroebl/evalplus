import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = 0
    minSums = []
    for num in nums:
        sum+=num
        minSums.append(sum)
    minSums = [math.inf for i in nums]
    minSums[0] = nums[0]
    for i in range(1,len(nums)):
        minSums[i]=min(minSums[i-1]+nums[i],nums[i])
    return min(minSums)
