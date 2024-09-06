import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min = math.inf
    start = 0
    end = 0

    # 1. Loop through the array nums
    # 2. For each element in the array nums, try to grow our window
    # 3. If our window grows past the minimum size, see if its current sum beats our minimum
    # 4. If our window grows past the end of the array, shrink it until it just fits in the array
    # 5. Return the smallest sum found

    while end < len(nums):
        # if our window grows past the minimum size, see if its current sum beats our minimum
        currSum = 0
        for i in range(start, end + 1):
            currSum += nums[i]
        if end - start + 1 >= 2 and currSum < min:
            min = currSum
        end += 1
        # if our window grows past the end of the array, shrink it until it just fits in the array
        if end == len(nums):
            end = start + 1
            start += 1
    return min
