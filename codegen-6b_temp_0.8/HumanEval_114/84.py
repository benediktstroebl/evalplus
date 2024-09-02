import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    """
    solution 1:
    sum = 0
    min_sum = 10**9
    for i in range(len(nums)):
        sum += nums[i]
        min_sum = min(min_sum, sum)
    return min_sum
    """

    """
    solution 2:
    n = len(nums)
    s = sum(nums)
    min_sum = s
    for i in range(n):
        s -= nums[i]
        if s < min_sum:
            min_sum = s
        s += nums[i+1]
    return min_sum
    """

    """
    solution 3:
    n = len(nums)
    min_sum = 0
    if n == 0:
        min_sum = 0
    elif n == 1:
        min_sum = nums[0]
    else:
        for i in range(n):
            min_sum = min(min_sum, min(nums[i], min_sum + nums[i]))
    return min_sum
    """

    """
    solution 4:
    n = len(nums)
    s = sum(nums)
    min_sum = s
    for i in range(n):
        min_sum = min(min_sum, s - nums[i] + nums[i+1])
    return min_sum
    """

    """
    solution 5:
    """
    if nums is None or len(nums) == 0:
        return 0
    min_sum = 0
    max_sum = 0
    for num in nums:
        max_sum = max(max_sum + num, 0)
        min_sum += max_sum
    return min_sum

