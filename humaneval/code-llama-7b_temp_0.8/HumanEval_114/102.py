import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def minSubArraySum_aux(nums, start, end):
        if nums[start] < nums[end]:
            return nums[start]
        elif nums[start] == nums[end]:
            return nums[start]
        else:
            if start == end:
                return nums[start]
            else:
                return minSubArraySum_aux(nums, start+1, end)

    # recursively calling function in range of nums list
    return minSubArraySum_aux(nums, 0, len(nums)-1)

