import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 1. if first element is 0, give it a weight of 1
    # 2. if element is negative, keep the negative value at the back, 
    #    for every positive number in the front
    # 3. if 0 is in nums, add 0 to the start of nums
    # 4. if there is a zero that is not the front or back, the subarray of 0s can be ignored
    if not nums:
        return None
    res = float('inf')
    for i in range(len(nums)):
        res = min(res, nums[i] + nums[i-1] if i > 0 else nums[i], nums[i])
    return res if res < float('inf') else None
