import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    start = 0
    for end in range(len(nums)):
        sum_ = 0
        for i in range(end, len(nums)):
            sum_ += nums[i]
            if sum_ < min_sum:
                min_sum = sum_
                start = i
        print(f"sum is {sum_}")
    
