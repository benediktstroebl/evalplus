import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_sum = max(sum(nums) for nums in product(*nums))
    for i in range(1, len(nums)):
        for j in range(i):
            for k in range(j, len(nums)):
                # check if there is a sub-array with length j-i+1
                if len(nums[j-i+1:j]) == j-i+1:
                    # check if the sum is smaller than max_sum
                    if sum(nums[j-i+1:j]) < max_sum:
                        return sum(nums[j-i+1:j])
    return max_sum
