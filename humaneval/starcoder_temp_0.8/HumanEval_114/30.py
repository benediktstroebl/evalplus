import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    if not nums:
        return 0
        
    # if array length is 1, min value is itself
    if len(nums) == 1:
        return nums[0]
    
    # if array length is 2, min value is the smallest two elements
    if len(nums) == 2:
        return min(nums[0], nums[1])
    
    # use kadane's algorithm
    # https://en.wikipedia.org/wiki/Maximum_subarray_problem
    # O(n)
    #
    # linear time and linear space
    # max_ending_here is the maximum sum up to index i (the first element index)
    # max_so_far is the maximum sum from index i to the end
    #
    # max_ending_here = max(max_ending_here + nums[i], nums[i])
    # max_so_far = max(max_so_far, max_ending_here)
    max_ending_here = nums[0]
    max_so_far = nums[0]
    for i in range(1, len(nums)):
        max_ending_here = max(max_ending_here + nums[i], nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
