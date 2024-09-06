import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # for i in range(0, len(nums)):
    #     for j in range(i, len(nums)):
    #         print(nums[i:j+1])
    #         print(sum(nums[i:j+1]))
    #         print(j-i+1)
    #         if (sum(nums[i:j+1]) < 0):
    #             print("inside", sum(nums[i:j+1]), j-i+1)
    #             print("--------------------------------------")
    #         else:
    #             print("outside")
    #             print("--------------------------------------")
    #         print("--------------------------------------")
    if len(nums) == 0:
        return 0

    minSum = math.inf
    subArraySum = 0
    for i in range(0, len(nums)):
        subArraySum += nums[i]
        minSum = min(minSum, subArraySum)
        if subArraySum < 0:
            subArraySum = 
