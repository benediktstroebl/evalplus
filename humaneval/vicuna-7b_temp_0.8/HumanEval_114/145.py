import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 1, nums[0]
    for i in range(1, len(nums)):
        if nums[i] < nums[left]:
            left = i
        else:
            right = i
    answer = max(left, right)
    for i in range(left, len(nums)):
        j = i
        while j < len(nums) and nums[j] <= right:
            j += 1
        if j - left + 1 not in [0, 1]:
            answer = max(answer, (j - left + 1))
    return answer
