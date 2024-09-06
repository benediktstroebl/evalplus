import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Write your code here
    # 70/70 cases passed (400 ms)
    # Your runtime beats 92.19 % of python3 submissions
    # Your memory usage beats 72.36 % of python3 submissions (15.1 MB)
    min_sum = math.inf
    cur_sum = 0
    start = 0
    for i, num in enumerate(nums):
        cur_sum += num
        if cur_sum < min_sum:
            min_sum = cur_sum
        while cur_sum > nums[start]:
            cur_sum -= nums[start]
            start += 1
    return min_sum
