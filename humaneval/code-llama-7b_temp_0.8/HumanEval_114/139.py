import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return min(nums[0], nums[1])
    
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            # print(i, j)
            sub = sum(nums[i:j])
            # print(sub)
            if sub < 0:
                min_sub = sub
            else:
                if min_sub == None:
                    min_sub = sub
                else:
                    if min_sub > sub:
                        min_sub = sub

    return min_sub
