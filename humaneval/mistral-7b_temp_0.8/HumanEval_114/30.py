import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 注意： 0 是合法的值，那么数组不是空的，但是，我们还是应该把这个区间的长度也返回给用户
    result = []
    min_num = math.inf
    for i in range(len(nums)):
        start_idx = i
        min_value = 0
        end_idx = i
        while end_idx < len(nums):
            # 注意： 如果这里的 min_value 是负数的话，那么我们不需要去更新 result
            min_value += nums[end_idx]
            if min_value < min_num:
                result = [start_idx, end_idx]
                min_num = min_value
            end_idx += 1
    return result



