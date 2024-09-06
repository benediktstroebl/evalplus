import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # O(n^2)
    def subarraySum(nums):
        min_sum = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = 0
                for k in range(i, j + 1):
                    sum += nums[k]
                min_sum = min(min_sum, sum)
        return min_sum
    print(subarraySum(nums))

